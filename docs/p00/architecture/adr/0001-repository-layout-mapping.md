# ADR-0001: P00 Repository Layout Mapping

- Status: Accepted
- Date: 2026-07-06
- Project: P00 — Introduction to Cybersecurity Engineering
- Branch: `p00-execution`
- Baseline commit: `6a77fb5`

## Context

The P00 reference model describes `enterprise-cybersecurity-lab/` as the
logical root of the complete laboratory and proposes dedicated directories
for services, security modules, orchestrators, attack scenarios, schemas,
tests, fixtures, architecture, documentation, evidence, and public artifacts.

The existing repository already has a public-safe domain structure:

- `controlled-adversary-emulation/`
- `detection-engineering/`
- `devsecops-security-qa/`
- `incident-response-automation/`
- `infrastructure-security/`
- `sample-data/`
- `docs/`

Creating duplicate top-level directories such as `red-team/`,
`documentation/`, or `architecture/` would fragment navigation and create
two competing representations of the same capabilities.

## Decision

The repository root is the physical equivalent of the logical
`enterprise-cybersecurity-lab/` root.

| Logical P00 path | Repository path | Decision |
|---|---|---|
| `enterprise-cybersecurity-lab/` | `./` | Reuse repository root |
| `documentation/p00/` | `docs/p00/` | Use existing documentation root |
| `architecture/c4/` | `docs/p00/architecture/c4/` | Create when diagrams are produced |
| `architecture/dfd/` | `docs/p00/architecture/dfd/` | Create when diagrams are produced |
| `architecture/adr/` | `docs/p00/architecture/adr/` | Use for P00 architecture decisions |
| `modules/service/p00-demo/` | `modules/service/p00-demo/` | New service path, created during S1 |
| `modules/defense/p00-file-defense/` | `infrastructure-security/p00-file-defense/` | Use existing Defense domain |
| `modules/detection/p00-file-integrity/` | `detection-engineering/p00-file-integrity/` | Use existing Detection domain |
| `modules/investigation/p00-config-tampering/` | `incident-response-automation/p00-config-tampering/` | Use existing Investigation domain |
| `red-team/scenarios/p00-config-tampering/` | `controlled-adversary-emulation/scenarios/p00-config-tampering/` | Use existing controlled LAB-emulation domain |
| `tests/` | `devsecops-security-qa/p00/tests/` | Keep QA assets in the existing QA domain |
| `fixtures/config/` | `sample-data/p00/config/` | Sanitized configuration fixtures |
| `fixtures/audit/` | `sample-data/p00/audit/` | Sanitized audit fixtures |
| `fixtures/recorded-attack/` | `sample-data/p00/recorded-attack/` | Sanitized recorded LAB fixtures |
| `lab/` | `lab/p00/` | New local LAB definitions and setup scripts |
| `schemas/` | `schemas/` | Shared versioned contracts |
| `orchestrators/` | `orchestrators/` | Thin integration layers only |
| `evidence/` | `evidence/p00/` | Index and sanitized public-safe evidence only |
| `public/` | `docs/p00/public/` | Public release material |
| `versions.lock` | `versions.lock` | Shared version record at repository root |
| `pyproject.toml` | `pyproject.toml` | Shared Python project metadata at repository root |

## Evidence Boundary

Raw LAB evidence, credentials, private keys, VM snapshots, packet captures
containing sensitive data, and unsanitized logs must not be committed.

The repository may contain only:

- evidence indexes;
- hashes;
- synthetic fixtures;
- sanitized excerpts;
- public-safe screenshots;
- reproducible instructions.

Raw evidence remains outside the public repository or inside an ignored local
LAB storage location.

## Consequences

- Existing domain directories are preserved.
- No mass file relocation is performed during P00.
- New directories are created only when their corresponding P00 stage begins.
- `controlled-adversary-emulation/` remains the Attack-domain owner.
- Orchestrators remain thin and do not duplicate module business logic.
- A future repository-wide restructuring requires a separate ADR.
- This mapping changes physical paths only; it does not change P00 scope,
  requirements, attack mode, Run A/B logic, or Definition of Done.

## Deferred Decisions

The following items are intentionally deferred until their implementation
stage:

- exact Python package layout;
- schema identifiers and versioning;
- evidence index format;
- LAB provisioning backend;
- CI workflow layout;
- release packaging format.