# Enterprise Cybersecurity Lab

![Lab Only](https://img.shields.io/badge/Scope-Isolated%20LAB-lightgrey)
![Program](https://img.shields.io/badge/Program-P00--P20-blue)
![Roles](https://img.shields.io/badge/Roles-R01--R26-blue)
![Status](https://img.shields.io/badge/Status-Migration%20Candidate-yellow)

## Purpose

This repository is the public-safe engineering workspace for the Enterprise Cybersecurity Program.

The program builds one evolving laboratory across P00–P20 and demonstrates how security capabilities are designed, delivered, defended, tested, attacked inside owned LAB scope, investigated, recovered and independently verified.

This repository is not a production toolkit and not a toolkit for unauthorized activity.

## Program architecture

```text
P00–P20 projects
      │
      ├── R01–R26 role modules
      │
      ├── ECP Scenario Controller
      │       └── Orchestration Core
      │
      ├── Delivery Orchestrator
      ├── Defense Orchestrator
      ├── Attack Orchestrator
      ├── Investigation Orchestrator
      ├── Recovery Orchestrator
      └── Assurance Orchestrator
              │
              ▼
      Domain modules, adapters and real tools
              │
              ▼
          Isolated Enterprise LAB
```

## Learning method

Each project uses a two-pass theory model:

1. complete reading of the current project's primary literature and assigned ranges;
2. targeted rereading of the relevant material and official documentation before each practical action.

The engineering cycle is:

`theory → design → baseline → Run A → investigation → remediation → comparable Run B → recovery → assurance → public-safe portfolio`

Every practical action must retain a concrete external source.

## Repository navigation

| Area | Directory | Purpose |
|---|---|---|
| Governance | [`governance/`](governance/) | Active canon, taxonomy, learning model and source authority |
| Migration | [`migration/`](migration/) | Migration plan, acceptance gates and rollback rules |
| Projects | [`projects/`](projects/) | P00–P20 technical manifests and scenarios |
| Roles | [`roles/`](roles/) | R01–R26 role-module model |
| Career | [`career/`](career/) | Career profiles and evidence-to-market mapping |
| Orchestration | [`orchestration/`](orchestration/) | Controller, Core and six domain orchestrators |
| Stack | [`stack/`](stack/) | Normalized product/component registry and version policy |
| Detection Engineering | [`detection-engineering/`](detection-engineering/) | Detection content and validation assets |
| Incident Response Automation | [`incident-response-automation/`](incident-response-automation/) | Investigation and response automation |
| Infrastructure Security | [`infrastructure-security/`](infrastructure-security/) | Linux, Windows and network security modules |
| Controlled LAB Emulation | [`controlled-adversary-emulation/`](controlled-adversary-emulation/) | LAB-only adversary scenarios and safe fixtures |
| DevSecOps / Security QA | [`devsecops-security-qa/`](devsecops-security-qa/) | Delivery, testing and assurance assets |
| Sample Data | [`sample-data/`](sample-data/) | Synthetic and sanitized fixtures |
| Documentation | [`docs/`](docs/) | Architecture, ADR, portfolio and safety documentation |

## Key documents

- [`governance/ACTIVE_CANON.md`](governance/ACTIVE_CANON.md)
- [`governance/program-taxonomy.yaml`](governance/program-taxonomy.yaml)
- [`governance/learning-model.md`](governance/learning-model.md)
- [`migration/2026-08-04-full-migration-plan.md`](migration/2026-08-04-full-migration-plan.md)
- [`docs/architecture/adr/0002-program-v12-migration.md`](docs/architecture/adr/0002-program-v12-migration.md)
- [`docs/p00/P00_CANON_V12.md`](docs/p00/P00_CANON_V12.md)
- [`orchestration/README.md`](orchestration/README.md)
- [`docs/portfolio_overview.md`](docs/portfolio_overview.md)
- [`docs/safety_and_scope.md`](docs/safety_and_scope.md)

## Evidence model

A completed project must produce:

- machine-readable run and evidence manifests;
- human-readable execution, incident, recovery and assurance reports;
- private raw evidence stored outside the public repository;
- sanitized public-safe case studies and fixtures.

Git, LAB execution, tests and evidence are the source of truth. A document or spreadsheet does not prove execution by itself.

## Current status

- v12 architecture: migrated to this branch;
- P00 canonical design: migration candidate;
- Controller and six orchestrators: designed, not implemented;
- LAB execution: not started under v12;
- Assurance PASS: not achieved;
- source workbook: preserved externally and not overwritten.

## Safety

All experiments are restricted to owned systems, local virtual machines, isolated LAB networks and synthetic or sanitized data.

Do not commit credentials, private keys, production logs, real intercepted traffic, malware samples, full packet captures, personal data or unsanitized evidence.

## Author

Ilya Berestov
