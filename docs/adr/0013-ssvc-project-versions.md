---
status: "accepted"
date: 2025-09-15
---
# SSVC Project Versions Follow Calendar Versioning (CalVer)

## Context

Individual SSVC objects (decision points, tables, etc.) use Semantic Versioning (SemVer).  
For the overall SSVC project and documentation, we need a scheme that better reflects frequent, incremental updates and communicates recency to users.

## Decision Drivers

- Object-level changes use SemVer, but the project evolves more fluidly.  
- Documentation often changes without altering underlying objects.  
- Users need clear signals about how current the materials are.

## Options

- **CalVer** for project and documentation  
- **SemVer** for project and documentation (status quo)

## Decision

**Chosen:** CalVer (`YYYY.MM.patch`)  

- **Major (`YYYY`) and minor (`MM`)** = release year and month  
  - First significant update in a month → `YYYY.M.0` (e.g., June 2025 → `2025.6.0`)  
- **Patch** = subsequent updates in the same month or smaller corrections  

**Significant updates** include:  

- Adding or restructuring sections in ways that affect usability  
- Adding/revising decision points, tables, or other SSVC objects  
- Adding features that change how SSVC is applied  

We expect ~1–4 `YYYY.MM` releases per year, with patches as needed.  
Months use single digits (`2025.6`) to keep versions concise.

## Rationale

CalVer suits SSVC’s character as a living framework:  

- Clearly signals recency (date in the version number)  
- Fits both documentation-focused and object-focused updates  
- Avoids SemVer debates over what counts as “major” or “minor”  

Individual SSVC objects will continue to use SemVer for backward compatibility.  

PyPI releases are expected to follow a similar CalVer scheme, but may include higher-resolution
date-time stamps for individual builds (e.g., `2025.6.141053`).

## Consequences

- **Good:** Versions clearly indicate recency and distinguish project vs. object evolution  
- **Neutral:** CalVer conveys less about compatibility, but SemVer at the object level mitigates this  
- **Bad:** Breaks continuity with past project-level SemVer (e.g., SSVC 1.x, 2.x)  

## Confirmation

The CalVer scheme will be applied via Git tags and GitHub releases.  

## Alternatives Rejected

**Continue SemVer for project/docs**  

- **Good:** Maintains continuity  
- **Bad:** Cannot easily express documentation updates independent of object versions  

## References

- [SSVC Decision Point Versioning Rules](0003-ssvc-decision-point-versioning-rules.md)
- [CalVer](https://calver.org/)  
- [SemVer](https://semver.org/)  
