---
status: "accepted"
date: 2025-09-15
---
# SSVC Project versions follow Calendar Versioning (CalVer)

## Context and Problem Statement

While individual SSVC objects (e.g., decision points, decision tables, etc.)
follow Semantic Versioning (SemVer), we need a way to version the overall SSVC 
project and documentation that reflects the pace of change and the nature of 
changes being made. 

<!-- This is an optional element. Feel free to remove. -->
## Decision Drivers

- SSVC objects use SemVer, but these objects are more granular than the overall project.
- The SSVC project and documentation are updated frequently, often with minor changes.
- Users need a clear understanding of the recency and relevance of the SSVC documentation.

## Considered Options

- Use Calendar Versioning (CalVer) for the SSVC project and documentation.
- Continue using Semantic Versioning (SemVer) for the SSVC project and documentation.

## Decision Outcome

Chosen option: Use Calendar Versioning (CalVer) for the SSVC project and documentation.

We will use the format YYYY.MM.patch.

Major (YYYY) and minor (MM) versions reflect the year and month of the release.

The first significant update in a given year/month is tagged as YYYY.M.0.

Example: If the first major revision in 2025 occurs in June, the version will be 2025.6.0.

Patch (patch) versions increment for:

Additional significant updates within the same month (rare, but possible).

Smaller corrections or clarifications released after the original YYYY.MM.0.

Significant updates are those that:

Add new sections or restructure documentation in ways that affect usability.

Introduce or substantially revise decision points, decision tables, or other SSVC objects.

Add features or capabilities that change how SSVC is applied.

We expect one to four YYYY.MM releases per year, with patch releases as needed.
Months will be represented as single digits (e.g., 2025.6 for June) to keep version strings concise.

Rationale:
CalVer aligns with SSVC’s nature as a living framework that evolves through both frequent minor edits and occasional substantial changes. While individual SSVC objects follow SemVer, the project as a whole benefits from a date-based scheme that reflects an ongoing, fluid update cycle.

Compared to SemVer, CalVer:

Better communicates the recency of releases (the version number encodes date).

Matches the balance of code-focused and documentation-focused updates.

Reduces the overhead of deciding what constitutes a “major” vs. “minor” release in a traditional SemVer sense.

<!-- This is an optional element. Feel free to remove. -->
### Consequences

- Good, because SSVC versions will clearly indicate the recency of the documentation and overall project state.
- Good, because it makes it easier to be clear about the distinction between the
  evolution of the SSVC framework and the specific versions of individual SSVC objects it contains.
- Neutral, because CalVer does not convey as much information about backward compatibility as SemVer.
  However, we mitigate this through the use of SemVer for individual SSVC objects.
- Bad, because we lose continuity with the previous SemVer scheme for the overall project (SSVC 1.0, 1.1, 2.0, 2.1)

<!-- This is an optional element. Feel free to remove. -->
### Confirmation

The main SSVC versioning scheme will be implemented via Git tags and in the `releases`
section of the SSVC GitHub repository.

<!-- This is an optional element. Feel free to remove. -->
## Pros and Cons of the Options

### Continue using Semantic Versioning (SemVer) for the SSVC project and documentation.

- Good, because it maintains continuity with the previous versioning scheme.
- Bad, because there is no clear way to show a significant documentation update
  that does not alter the version of any individual SSVC object.


<!-- This is an optional element. Feel free to remove. -->
## More Information

- [SSVC Decision Point Versioning Rules](0003-ssvc-decision-points-are-versioned.md)
- [Calendar Versioning (CalVer)](https://calver.org/)
- [Semantic Versioning (SemVer)](https://semver.org/)