"""LLM-optimized export for the spec registry.

Produces a flat, inheritance-resolved JSON projection designed for
coding agent consumption.  Requirements become primary objects with
denormalized group/file provenance and resolved kind/scope/tags.

Usage::

    from ssvc.metadata.specs.registry import load_registry
    from ssvc.metadata.specs.llm_export import to_llm_json

    registry = load_registry()
    # All specs
    print(to_llm_json(registry))
    # Single topic
    print(to_llm_json(registry, topic="SR"))
    # Specific IDs with transitive dependencies
    print(to_llm_json(registry, spec_ids=["SR-01-001"], include_deps=True))
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
from typing import Any

from ssvc.metadata.specs.registry import (
    SpecRegistry,
    effective_kind,
    effective_scope,
    effective_tags,
)
from ssvc.metadata.specs.schema import (
    BehavioralSpec,
    Spec,
    SpecFile,
    SpecGroup,
)


def _spec_record(
    spec: Spec,
    group: SpecGroup,
    file: SpecFile,
) -> dict[str, Any]:
    """Build a flat, inheritance-resolved dict for a single spec."""
    rec: dict[str, Any] = {
        "id": spec.id,
        "topic": file.id,
        "group": group.id,
        "group_title": group.title,
        "type": (
            "behavioral" if isinstance(spec, BehavioralSpec) else "statement"
        ),
        "priority": spec.priority.value,
        "statement": spec.statement,
        "kind": effective_kind(spec, group, file).value,
        "scope": [s.value for s in effective_scope(spec, group, file)],
    }

    tags = effective_tags(spec)
    if tags:
        rec["tags"] = [t.value for t in tags]

    if spec.rationale is not None:
        rec["rationale"] = spec.rationale

    if not spec.testable:
        rec["testable"] = False

    if spec.relationships:
        rec["relationships"] = [_rel_record(r) for r in spec.relationships]

    if isinstance(spec, BehavioralSpec):
        if spec.preconditions:
            rec["preconditions"] = [p.description for p in spec.preconditions]
        if spec.steps:
            rec["steps"] = [_step_record(s) for s in spec.steps]
        if spec.postconditions:
            rec["postconditions"] = [
                p.description for p in spec.postconditions
            ]

    return rec


def _rel_record(r: object) -> dict[str, str]:
    d: dict[str, str] = {
        "rel_type": r.rel_type.value,  # type: ignore[attr-defined]
        "spec_id": r.spec_id,  # type: ignore[attr-defined]
    }
    if r.note is not None:  # type: ignore[attr-defined]
        d["note"] = r.note  # type: ignore[attr-defined]
    return d


def _step_record(s: object) -> dict[str, Any]:
    d: dict[str, Any] = {
        "order": s.order,  # type: ignore[attr-defined]
        "actor": s.actor,  # type: ignore[attr-defined]
        "action": s.action,  # type: ignore[attr-defined]
    }
    if s.expected is not None:  # type: ignore[attr-defined]
        d["expected"] = s.expected  # type: ignore[attr-defined]
    return d


def _topic_record(file: SpecFile) -> dict[str, str]:
    return {
        "id": file.id,
        "title": file.title,
        "version": file.version,
        "kind": file.kind,
    }


def _selected_spec_ids(
    registry: SpecRegistry,
    spec_ids: list[str] | None,
    *,
    include_deps: bool,
) -> set[str] | None:
    if spec_ids is None:
        return None

    selected_ids = set(spec_ids)
    if include_deps:
        for spec_id in list(selected_ids):
            selected_ids |= registry.transitive_deps(spec_id)
    return selected_ids


def _matches_filters(
    spec: Spec,
    group: SpecGroup,
    file: SpecFile,
    *,
    topic: str | None,
    selected_ids: set[str] | None,
    spec_id: str,
    kind: str | None,
    scope: str | None,
    tags: list[str] | None,
    priority: str | None,
) -> bool:
    if topic is not None and file.id != topic:
        return False
    if selected_ids is not None and spec_id not in selected_ids:
        return False

    eff_kind = effective_kind(spec, group, file)
    eff_scope_values = {
        item.value for item in effective_scope(spec, group, file)
    }
    eff_tag_values = {item.value for item in effective_tags(spec)}

    if kind and eff_kind.value != kind:
        return False
    if scope and scope not in eff_scope_values:
        return False
    if tags and not set(tags).issubset(eff_tag_values):
        return False
    if priority and spec.priority.value != priority:
        return False
    return True


def _edge_record(spec_id: str, relationship: object) -> dict[str, str]:
    edge: dict[str, str] = {
        "from": spec_id,
        "rel_type": relationship.rel_type.value,  # type: ignore[attr-defined]
        "to": relationship.spec_id,  # type: ignore[attr-defined]
    }
    if relationship.note:  # type: ignore[attr-defined]
        edge["note"] = relationship.note  # type: ignore[attr-defined]
    return edge


def to_llm_json(
    registry: SpecRegistry,
    *,
    topic: str | None = None,
    spec_ids: list[str] | None = None,
    include_deps: bool = False,
    kind: str | None = None,
    scope: str | None = None,
    tags: list[str] | None = None,
    priority: str | None = None,
) -> str:
    """Produce a flat, inheritance-resolved JSON projection of the registry.

    Args:
        registry: The loaded SpecRegistry.
        topic: Filter to specs from the file with this ID prefix.
        spec_ids: Filter to these specific spec IDs.
        include_deps: When True and *spec_ids* is given, expand to include
            transitive dependencies via the requirements graph.
        kind: Filter to specs with this effective kind value.
        scope: Filter to specs whose effective scope contains this value.
        tags: Filter to specs that have ALL of the given tags.
        priority: Filter to specs with this priority value.

    Returns:
        Compact JSON string (no indentation).
    """
    selected_ids = _selected_spec_ids(
        registry, spec_ids, include_deps=include_deps
    )
    requirements: list[dict[str, Any]] = []
    edges: list[dict[str, str]] = []
    topic_ids_seen: set[str] = set()

    for spec_id, spec in registry.all_specs.items():
        group, file = registry._spec_context[spec_id]
        if not _matches_filters(
            spec,
            group,
            file,
            topic=topic,
            selected_ids=selected_ids,
            spec_id=spec_id,
            kind=kind,
            scope=scope,
            tags=tags,
            priority=priority,
        ):
            continue

        requirements.append(_spec_record(spec, group, file))
        topic_ids_seen.add(file.id)
        edges.extend(
            _edge_record(spec_id, relationship)
            for relationship in spec.relationships or []
        )

    result: dict[str, Any] = {
        "topics": [
            _topic_record(file)
            for file in registry.files
            if file.id in topic_ids_seen
        ],
        "requirements": requirements,
        "edges": edges,
    }
    return json.dumps(result, separators=(",", ":"))
