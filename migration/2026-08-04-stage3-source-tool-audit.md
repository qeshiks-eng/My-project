# Stage 3 · Source quality, tool pins and P00 sequence

Status: `MIGRATION_CANDIDATE_STAGE3`

## Completed

- Reordered P00 repair blocks into the actual learning sequence.
- Verified 17 critical stable/security tool baselines against official release sources.
- Added 416 version annotations across 366 tool cells.
- Built a registry for 815 unique URLs and 4436 URL occurrences.
- Classified source authority, repository pin status, broad-index risk and live-verification scope.
- Built a route-level registry for 248 tool labels across 853 assignments.
- Reviewed repeated rows: cross-project orchestrator and R25 rows are reusable templates, not automatic duplicate defects.

## Current blockers

- 136 GitHub URLs still require immutable release tag or commit SHA before the corresponding LAB run.
- 150 broad-index URLs require an exact chapter, section or lab link.
- Full live review of all 815 unique URLs is not complete.
- Route labels are not yet decomposed into a canonical unique-product registry.
- P00 LAB execution is `NOT_STARTED`.
- P15-P20 remain semantic rebuilds rather than byte-identical legacy hydration.

## Truth statement

Stage 3 improves the learning library and source/tool controls. It does not prove execution, operational experience or P00 PASS. The v12 candidate must not be marked ACTIVE until the remaining source gates and the real LAB cycle are completed.
