# Priorities

## Important note about priority numbers

Priority numbers are ascending, so lower numbers are higher priority.
The scale is not linear, it's just intended to provide a rough ordering and
allow for space between to add new priorities in the future if needed. The
priority numbers themselves do not have any inherent meaning beyond their
relative order. Completed priorities should be archived via `uv run append-history priority`
(writes to `plan/history/YYMM/priority/`) and then removed from this file to keep
`plan/PRIORITIES.md` focused on pending and in-progress work.

Each priority group should have a corresponding GitHub Issue of type `Epic`
that tracks the overall work as child issues (which may in turn have their
own child issues, etc.) The list of child issues in GitHub is
authoritative regardless what is listed below, this file is a high-level
index and summary.

## Priority 100

