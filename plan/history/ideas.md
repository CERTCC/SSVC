
---

## IDEA-902: Do we still need Decision Point Groups now that we have DecisionTable?

**Title:** Do we still need Decision Point Groups now that we have `DecisionTable`?

**Body:**

Decision Point Groups are basically just a list of Decision Point objects that can have their own name, description, and version associated with the collection. Their primary use has been as a stand-in prior to us having a full `DecisionTable` object.

However, now we have the following ways to group Decision Points:

1. In a `DecisionTable`, the relevant `DecisionPoint` objects are included directly, so there is no question which decision points are relevant to the specific decision.
2. In the `SsvcObjectRegistry`, you can extract collections of `DecisionPoint` objects by namespace.

Because of (1), some Decision Point Group modules seem redundant:

| Decision Point Group Module | Decision Table Module |
|---|---|
| `ssvc/dp_groups/ssvc/supplier.py` | `ssvc/decision_tables/ssvc/supplier_dt.py` |
| `ssvc/dp_groups/ssvc/deployer.py` | `ssvc/decision_tables/ssvc/deployer_dt.py` |
| `ssvc/dp_groups/ssvc/coordinator_triage.py` | `ssvc/decision_tables/ssvc/coord_triage.py` |
| `ssvc/dp_groups/ssvc/coordinator_publication.py` | `ssvc/decision_tables/ssvc/coord_pub_dt.py`|

Proposed:
1. Eliminate the four redundant Decision Point Group modules (and collections.py)
2. Remove base.py once all callers are migrated
3. Migrate policy_generator.py to use DecisionTable
4. Remove doctools.py dump_schemas DecisionPointGroup entry
5. Block CVSS collections removal on issues #922, #923, #924
6. Ship Phase 1 as a major version bump

**Processed**: 2026-05-18 — design decisions captured in `specs/dp-groups-removal.yaml` and `notes/dp-groups-removal.md`.
