# Full Program Migration · 2026-08-04

## Objective

Migrate the Enterprise Cybersecurity Program to the v12 architecture without losing theory, practice, tools, sources, role responsibilities, evidence requirements or historical traceability.

## Non-negotiable rules

- Preserve the RC3.7.0 source workbook unchanged.
- Do not reduce content merely to make the library smaller.
- Do not merge administrative governance into learner-facing PXX content.
- Do not replace real practice with overview-only exercises.
- Do not treat design coverage as completed study.
- Do not make AI mandatory for orchestration.
- Do not publish private raw evidence.
- Do not delete superseded material until migration traceability and rollback are proven.

## Target architecture

- P00–P20.
- R01–R26.
- Role, role module and career profile separated and traceable.
- ECP Scenario Controller.
- Shared Orchestration Core.
- Six first-class domain orchestrators.
- Two-pass theory.
- Real LAB practice with external sources.
- Run A, Investigation, remediation, comparable Run B, Recovery and Assurance.
- Private, machine-readable, human-readable and public-safe evidence layers.

## Migration phases

### M00. Source freeze

Status: `PARTIAL`

Completed:

- RC3.7.0 filename and SHA-256 registered.
- Source remains immutable.
- Repository migration branch created.

Required before binary library migration:

- mount or upload the exact RC3.7.0 workbook into the active execution environment;
- calculate local checksum and compare with the registered SHA-256;
- create a byte-identical backup.

### M01. Canon and terminology

Status: `COMPLETE_IN_REPOSITORY`

Created:

- `governance/ACTIVE_CANON.md`;
- `governance/program-taxonomy.yaml`;
- `governance/learning-model.md`;
- `governance/source-authority.yaml`;
- ADR-0002.

### M02. Repository architecture

Status: `IN_PROGRESS`

Created:

- `projects/`;
- `roles/`;
- `career/`;
- `stack/`;
- `orchestration/`;
- `governance/`;
- `migration/`.

Existing domain directories remain in place. No destructive mass relocation is performed.

### M03. Orchestration migration

Status: `DESIGN_MIGRATED · IMPLEMENTATION_NOT_STARTED`

Created:

- Controller/Core architecture;
- scenario and run-context contracts;
- P00 Run A and Run B scenarios;
- domain responsibility model;
- deterministic decision policy.

Still required:

- implementation code;
- tests;
- CLI;
- evidence writer;
- adapters;
- real LAB validation.

### M04. P00 migration

Status: `CANON_MIGRATED · MATERIAL_REPAIR_REQUIRED`

Decisions:

- Introductory Ubuntu/Nginx case is the P00 core.
- Deep configuration/symlink-tampering case is preserved as P00-EXT-01.
- All six orchestrators receive a minimal real vertical slice.
- R01–R26 receive real, bounded contributions rather than overview labels.

Material gaps that must be repaired in the source library:

- exact network and snapshot route for L02;
- Bash detection engineering and deterministic fixtures for L05;
- deployment, backup, restore and acceptance route for L07;
- Russian primary path;
- exact source sequencing;
- evidence methodology and UTC handling.

### M05. Library row migration

Status: `BLOCKED_BY_SOURCE_BYTES`

Required actions after the source workbook is mounted:

1. import RC3.7.0 without modifying it;
2. create v12 migration candidate and byte-identical backup;
3. add stable IDs and migration lineage;
4. retain all P01–P20 rows;
5. migrate P00 cards to two-pass theory and six-orchestrator model;
6. replace overview role labels with real contribution records;
7. preserve all source URLs and mark replacements explicitly;
8. separate governance metadata from learner-facing content;
9. preserve formulas, formatting and row heights where still applicable;
10. produce row-level migration map.

### M06. Stack normalization

Status: `SEED_CREATED`

Created:

- registry model;
- schema;
- P00 and internal platform seed entries.

Still required:

- normalize all P01–P20 assignments;
- deduplicate aliases;
- distinguish products, components, libraries and specifications;
- calculate unique product and component counts;
- preserve the original assignment count.

### M07. Career migration

Status: `MODEL_MIGRATED`

Still required:

- create R01–R26 career profile records;
- map projects and artifacts to vacancy families;
- preserve private personal filters outside the public repository;
- validate resume statements against actual evidence.

### M08. Acceptance audit

Status: `NOT_STARTED`

The target version may become ACTIVE only after all gates pass.

## Acceptance gates

### A01. Structural preservation

- exactly 21 projects;
- exactly 26 roles;
- no missing project sheet;
- no broken formulas;
- no accidental blank labels;
- no untraceable deletions.

### A02. Theory

- primary project literature supports the complete first pass;
- assigned book pages and editions are retained;
- targeted rereading is mapped to practical phases;
- Russian route is primary where available;
- official original source remains traceable.

### A03. Practice

- every practical action has an external source;
- real LAB action, artifacts, tests and evidence are specified;
- attack, defense, investigation, recovery and assurance are not artificially weakened;
- cleanup and rollback are explicit.

### A04. Roles

- every P00–P18 project reviews R01–R26;
- applicable roles have real contributions;
- exceptional N/A has rationale;
- reviewer/approver/evidence/handoff responsibilities remain traceable;
- no implementer-only independent PASS.

### A05. Orchestration

- Controller and Core are separate from six domain orchestrators;
- orchestrators own process outcomes and may contain domain logic;
- stable contracts and run_id are used;
- arbitrary shell is not a public contract;
- safety scope cannot be disabled by a flag;
- AI has advisory authority only.

### A06. Evidence and portfolio

- raw/private and public-safe layers are separated;
- hashes, UTC, versions and lineage are preserved;
- Run A/Run B comparison exists;
- recovery is tested;
- public artifacts are sanitized.

### A07. Status truth

- designed, implemented, LAB-validated and PASS states are distinct;
- no document claims completed practice without execution evidence;
- lab experience is not described as commercial production experience.

## Rollback

If any acceptance gate fails:

- v12 remains `MIGRATION_CANDIDATE`;
- RC3.7.0 remains the source authority;
- the migration branch is not merged;
- defects are corrected and the audit is rerun;
- no source material is deleted.
