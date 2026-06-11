"""Context generation tool for the spec registry.

Provides a markdown renderer, a JSON exporter, and a YAML exporter for
agent/human consumption.

Usage::

    from pathlib import Path
    from ssvc.metadata.specs import load_registry
    from ssvc.metadata.specs.render import render_markdown, export_json

    registry = load_registry(Path("specs/"))
    md = render_markdown(registry.files[0])
    js = export_json(registry)
"""

#  Copyright (c) 2026 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from __future__ import annotations

import json
from pathlib import Path

from ssvc.metadata.specs.registry import (
    SpecRegistry,
    effective_tags,
    load_registry,
)
from ssvc.metadata.specs.schema import (
    BehavioralSpec,
    Spec,
    SpecFile,
    SpecGroup,
)

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "pyyaml is required for YAML export. "
        "Install it with: pip install pyyaml"
    ) from exc


def _priority_line(spec: Spec) -> str:
    return f"- `{spec.id}` {spec.statement}"


def _append_behavioral_markdown(
    lines: list[str], spec: BehavioralSpec
) -> None:
    for precondition in spec.preconditions or []:
        lines.append(f"  - *Precondition*: {precondition.description}")

    for step in spec.steps or []:
        lines.append(f"  - *Step {step.order}* [{step.actor}]: {step.action}")
        if step.expected:
            lines.append(f"    - *Expected*: {step.expected}")

    for postcondition in spec.postconditions or []:
        lines.append(f"  - *Postcondition*: {postcondition.description}")


def _append_relationship_markdown(lines: list[str], spec: Spec) -> None:
    for relationship in spec.relationships or []:
        note = f" ({relationship.note})" if relationship.note else ""
        lines.append(
            f"  - {spec.id} {relationship.rel_type.value} "
            f"{relationship.spec_id}{note}"
        )


def _append_spec_markdown(lines: list[str], spec: Spec) -> None:
    lines.append(_priority_line(spec))
    if spec.rationale:
        lines.append(f"  - *Rationale*: {spec.rationale}")
    if isinstance(spec, BehavioralSpec):
        _append_behavioral_markdown(lines, spec)
    _append_relationship_markdown(lines, spec)


def _append_group_markdown(lines: list[str], group: SpecGroup) -> None:
    lines.append(f"## {group.title}")
    lines.append("")
    if group.description:
        lines.append(group.description)
        lines.append("")
    for spec in group.specs:
        _append_spec_markdown(lines, spec)
    lines.append("")


def render_markdown(spec_file: SpecFile) -> str:
    """Render a single SpecFile as a Markdown string."""
    lines = [
        f"# {spec_file.title}",
        "",
        "## Overview",
        "",
        spec_file.description,
        "",
        f"**Version**: {spec_file.version}",
        "",
        "---",
        "",
    ]
    for group in spec_file.groups:
        _append_group_markdown(lines, group)
    return "\n".join(lines)


def _add_behavioral_spec_fields(d: dict, spec: BehavioralSpec) -> None:
    authored_sequences = {
        "preconditions": [
            {"description": item.description}
            for item in spec.preconditions or []
        ],
        "steps": [_step_dict(item) for item in spec.steps or []],
        "postconditions": [
            {"description": item.description}
            for item in spec.postconditions or []
        ],
    }
    for field, value in authored_sequences.items():
        if value:
            d[field] = value


def _spec_to_dict(spec: Spec, group: SpecGroup, file: SpecFile) -> dict:
    """Serialize a spec to a dict with only authored (non-inherited) fields."""
    _ = group, file
    d: dict = {
        "id": spec.id,
        "priority": spec.priority.value,
        "statement": spec.statement,
    }
    authored_optional_fields = {
        "rationale": spec.rationale,
        "kind": spec.kind.value if spec.kind is not None else None,
        "scope": (
            [s.value for s in spec.scope] if spec.scope is not None else None
        ),
        "tags": (
            [t.value for t in spec.tags] if spec.tags is not None else None
        ),
        "relationships": (
            [_rel_dict(relationship) for relationship in spec.relationships]
            if spec.relationships
            else None
        ),
        "lint_suppress": (
            [warning.value for warning in spec.lint_suppress]
            if spec.lint_suppress
            else None
        ),
    }
    for field, value in authored_optional_fields.items():
        if value is not None:
            d[field] = value
    if not spec.testable:
        d["testable"] = False
    if isinstance(spec, BehavioralSpec):
        _add_behavioral_spec_fields(d, spec)
    return d


def _rel_dict(r: object) -> dict:
    d = {
        "rel_type": r.rel_type.value,  # type: ignore[attr-defined]
        "spec_id": r.spec_id,  # type: ignore[attr-defined]
    }
    if r.note is not None:  # type: ignore[attr-defined]
        d["note"] = r.note  # type: ignore[attr-defined]
    return d


def _step_dict(s: object) -> dict:
    d = {
        "order": s.order,  # type: ignore[attr-defined]
        "actor": s.actor,  # type: ignore[attr-defined]
        "action": s.action,  # type: ignore[attr-defined]
    }
    if s.expected is not None:  # type: ignore[attr-defined]
        d["expected"] = s.expected  # type: ignore[attr-defined]
    return d


def _group_to_dict(group: SpecGroup, file: SpecFile) -> dict:
    """Serialize a group to a dict with only authored fields."""
    d: dict = {"id": group.id, "title": group.title}
    if group.description is not None:
        d["description"] = group.description
    if group.kind is not None:
        d["kind"] = group.kind.value
    if group.scope is not None:
        d["scope"] = [s.value for s in group.scope]
    d["specs"] = [_spec_to_dict(s, group, file) for s in group.specs]
    return d


def _file_to_dict(spec_file: SpecFile) -> dict:
    """Serialize a SpecFile to a dict with only authored fields."""
    return {
        "id": spec_file.id,
        "title": spec_file.title,
        "description": spec_file.description,
        "version": spec_file.version,
        "kind": spec_file.kind.value,
        "scope": [s.value for s in spec_file.scope],
        "groups": [_group_to_dict(g, spec_file) for g in spec_file.groups],
    }


class _YamlDumper(yaml.SafeDumper):
    """Custom YAML dumper with folded block scalars for long strings."""

    pass


def _str_representer(dumper: yaml.SafeDumper, data: str) -> yaml.ScalarNode:
    if "\n" in data or len(data) > 80:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style=">"
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_YamlDumper.add_representer(str, _str_representer)


def export_yaml(spec_file: SpecFile) -> str:
    """Serialize a single :class:`SpecFile` to authoritative YAML.

    Only authored fields are emitted — inherited defaults are omitted so
    that the YAML remains the canonical source of truth.
    """
    return yaml.dump(
        _file_to_dict(spec_file),
        Dumper=_YamlDumper,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
    )


def export_json(
    registry: SpecRegistry,
    *,
    kind: str | None = None,
    scope: str | None = None,
    tags: list[str] | None = None,
    priority: str | None = None,
) -> str:
    """Serialize the registry (or a filtered subset) to JSON.

    Args:
        registry: The loaded SpecRegistry.
        kind: Filter to specs with this kind value (e.g. ``"general"``).
        scope: Filter to specs whose scope list contains this value.
        tags: Filter to specs that have ALL of the given tags.
        priority: Filter to specs with this priority value (e.g. ``"MUST"``).

    Returns:
        A JSON string of the filtered spec index.
    """
    result = {}
    for spec_id, spec in registry.all_specs.items():
        eff_kind = registry.get_effective_kind(spec_id)
        eff_scope = registry.get_effective_scope(spec_id)
        eff_tags = effective_tags(spec)

        if kind and eff_kind.value != kind:
            continue
        if scope and scope not in [s.value for s in eff_scope]:
            continue
        if tags and not all(t in [tg.value for tg in eff_tags] for t in tags):
            continue
        if priority and spec.priority.value != priority:
            continue
        result[spec_id] = spec.model_dump(mode="json")

    return json.dumps(result, indent=2)


def render_registry_markdown(registry: SpecRegistry) -> str:
    """Render all spec files in the registry as concatenated Markdown."""
    parts = [render_markdown(f) for f in registry.files]
    return "\n\n---\n\n".join(parts)


def main() -> None:
    """CLI entry point for context generation.

    Usage::

        python -m ssvc.metadata.specs.render --format md specs/
        python -m ssvc.metadata.specs.render --format json specs/
        python -m ssvc.metadata.specs.render --format yaml specs/
        python -m ssvc.metadata.specs.render --format llm-json specs/
        python -m ssvc.metadata.specs.render --format llm-json --topic SR specs/
    """
    import sys

    fmt = "md"
    topic = None
    args = sys.argv[1:]
    if "--format" in args:
        idx = args.index("--format")
        fmt = args[idx + 1]
        args = args[:idx] + args[idx + 2 :]
    if "--topic" in args:
        idx = args.index("--topic")
        topic = args[idx + 1]
        args = args[:idx] + args[idx + 2 :]

    if not args:
        print(
            f"Usage: {sys.argv[0]} [--format md|json|yaml|llm-json]"
            " [--topic FILEID] <spec_dir>",
            file=sys.stderr,
        )
        sys.exit(2)

    spec_dir = Path(args[0])
    registry = load_registry(spec_dir)

    if fmt == "json":
        print(export_json(registry))
    elif fmt == "yaml":
        for sf in registry.files:
            print(export_yaml(sf))
            print("---")
    elif fmt == "llm-json":
        from ssvc.metadata.specs.llm_export import to_llm_json

        print(to_llm_json(registry, topic=topic))
    else:
        print(render_registry_markdown(registry))


def main_llm_json() -> None:
    """LLM-optimized spec dump entry point (``ssvc-spec-dump``).

    Exports all specs as flat, inheritance-resolved JSON for coding agents.
    Defaults to the ``specs/`` directory relative to the current working
    directory.

    Usage::

        ssvc-spec-dump
        ssvc-spec-dump specs/
    """
    import sys

    args = sys.argv[1:]
    spec_dir = Path(args[0]) if args else Path("specs")

    if not spec_dir.is_dir():
        print(
            f"Error: spec directory not found: {spec_dir}",
            file=sys.stderr,
        )
        sys.exit(2)

    from ssvc.metadata.specs.llm_export import to_llm_json

    registry = load_registry(spec_dir)
    print(to_llm_json(registry))


if __name__ == "__main__":
    main()
