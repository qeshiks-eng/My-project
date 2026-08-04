# Semantic Rebuild Stage 1 · 2026-08-04

## Result

A learner-facing workbook was generated outside the repository:

`12_LIBRARY_SCHEMA_P00-P20_v12.0_SEMANTIC_REBUILD_STAGE1.xlsx`

SHA-256:

`b420afe513d906342800898628f8ac71510114e682bf25db6ada99199167d79e`

Lineage JSON SHA-256:

`8a4ccedf9f080331a97a7d947c907f2ed423f98b46a1a03daaac246569130a73`

## Structure

- exactly 21 learner-facing sheets: P00–P20;
- no governance/audit sheets inside the learning library;
- columns remain Role/Stage, Theory, Practice and Tools;
- v12 two-pass theory and six-orchestrator lifecycle are present.

## Provenance

The uploaded RC3.7.0 file was truncated to 524288 bytes. Its complete local ZIP entries allowed direct semantic recovery of:

- P00–P13 complete cell values;
- P14 complete rows available through R03.

The remaining content was rebuilt as follows:

- P00: current introductory content retained and enriched with real bounded R01–R26 contributions plus Controller/Core/six-orchestrator ownership;
- P01–P13: recovered cell values retained and a v12 execution overlay added;
- P14: exact recoverable prefix retained and R04–R26 rebuilt at role level;
- P15–P20: complete role-level semantic routes rebuilt from File Library content, audits/crosswalks and the v12 canon;
- P18: Recovery route includes restic/Velero and preserves the recorded RC3.7.0 restic delta.

## Applied v12 rules

- complete first-pass reading of each project's primary route;
- targeted rereading immediately before practice;
- external source for each generated practice;
- technical manifest separate from program governance;
- Scenario Controller and shared Orchestration Core;
- Delivery, Defense, Attack, Investigation, Recovery and Assurance orchestrators;
- Run A, investigation, remediation, comparable Run B, recovery and Assurance;
- versions/commit SHA/image digest pinned immediately before LAB;
- design status does not imply learner execution or PASS.

## Limitation

This is a semantic rebuild and not a byte-identical restoration of RC3.7.0.

Exact historical rows for P15–P20 remain eligible for later hydration if a complete binary donor becomes available. Until then, the role-level v12 routes are usable as the migration candidate, while the original File Library files remain source authorities for comparison.

## Status change

`M05 Binary library rows` changes from `BLOCKED_BY_SOURCE_BYTES` to `SEMANTIC_REBUILD_STAGE1_COMPLETE`.

The candidate is not ACTIVE yet. Required next gates:

1. material audit of all P00–P20 sheets;
2. targeted repair of P00 L02/L05/L07 and Russian route;
3. URL/source precision audit;
4. duplicate and tool-registry normalization;
5. visual audit;
6. explicit promotion only after acceptance.
