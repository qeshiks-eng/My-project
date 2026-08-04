# ADR-0002: Enterprise Cybersecurity Program v12 Migration

- Status: Accepted for migration
- Date: 2026-08-04
- Scope: P00–P20, R01–R26, repository, orchestration, evidence and portfolio
- Migration branch: `program-migration-v12`

## Context

The program accumulated several partially incompatible representations:

- P00–P18 versus P00–P20;
- R01–R19 versus R01–R26;
- an older deep P00 based on configuration/symlink tampering;
- a newer introductory P00 based on a bounded Ubuntu/Nginx case;
- three original orchestrators versus the later six-orchestrator model;
- documents that mixed administrative control with learner-facing content;
- structural audits that passed while material-readiness audits still found gaps.

The repository ADR-0001 intentionally kept orchestrators thin and deferred package, schema and evidence decisions. The updated program now requires a formal cross-project orchestration platform without duplicating mature external tools.

## Decision

### 1. Program scope

The canonical program consists of P00–P20 and R01–R26.

- P00–P18 form the core sequence.
- P19 and P20 are specializations after P18.
- Each applicable role performs real work relative to the project scope.
- Overview-only role participation is not accepted as evidence of competence.

### 2. P00

The introductory Ubuntu/Nginx case becomes the migration baseline for P00 because it can teach the complete engineering cycle without importing specialization-level complexity.

The older configuration/symlink-tampering P00 is not deleted. It is reclassified as a preserved deep extension and may be used after the introductory P00 or reassigned to a later host-security/adversary-emulation/integration project.

P00 must include a minimal working vertical slice of:

- ECP Scenario Controller;
- Orchestration Core;
- Delivery;
- Defense;
- Attack;
- Investigation;
- Recovery;
- Assurance.

### 3. Orchestration architecture

There are six equal first-class domain orchestrators:

1. Delivery Orchestrator;
2. Defense Orchestrator;
3. Attack Orchestrator;
4. Investigation Orchestrator;
5. Recovery Orchestrator;
6. Assurance Orchestrator.

The ECP Scenario Controller is a coordinator, not a seventh domain orchestrator.

The Orchestration Core provides shared contracts, CLI conventions, configuration loading, run context, state machine, scope enforcement, evidence handling, logging, checkpoints, resume and handoff.

### 4. Domain ownership

Orchestrators are not empty wrappers around module flags.

They own the result of their process and may contain:

- workflow logic;
- decision rules;
- domain-specific analyzers;
- adapters;
- validation;
- reporting;
- evidence generation.

Low-level reusable capabilities remain in modules or external tools. Examples:

- Investigation owns PCAP analysis and may use tshark, Zeek, Suricata, Scapy or its own parser.
- Recovery owns backup and restore and may use restic, Borg, VMware API, Ansible or its own integrity logic.
- Delivery owns deployment and rollback while using Git, Ansible, CI/CD, IaC and package tools.

### 5. Decision model

The mandatory control path is deterministic:

- contracts;
- state machine;
- policy rules;
- thresholds;
- typed inputs;
- deterministic heuristics;
- human approval for ambiguous or high-risk actions.

AI is optional and advisory only. It cannot change scope, execute arbitrary shell commands, issue PASS, destroy evidence or assert root cause without supporting evidence.

### 6. Learning model

Each project uses two theory passes:

1. complete reading of the project's primary literature and assigned ranges;
2. targeted rereading and official documentation immediately before the related practical action.

Every practice item retains an external source.

### 7. Layer separation

Learner-facing PXX documents contain technical study and execution content only.

Program governance, migration records, release status, audits, market mapping and library administration remain in a separate governance layer.

### 8. Evidence boundary

The public repository stores only public-safe artifacts. Raw evidence remains in a private evidence vault.

### 9. Status truth

Design coverage does not prove implementation. Implementation does not prove LAB execution. LAB execution does not prove PASS until Assurance criteria are satisfied.

## Consequences

- ADR-0001 remains valid for preservation of existing domain directories and the public-safe boundary.
- The ADR-0001 statement that orchestrators are thin integration layers is narrowed: orchestration must not duplicate reusable low-level capabilities, but each orchestrator may and should own substantial workflow and domain logic.
- The repository gains governance, orchestration, project, role, career and stack registries without deleting existing domain directories.
- The binary learning library remains external and is referenced through hashes and migration records.
- A new version becomes ACTIVE only after source-preserving migration and acceptance audit.

## Acceptance conditions

- 21 projects and 26 roles are present.
- No theory, practice, tool assignment or source is silently deleted.
- Every practice retains an external source.
- Role, role module and career profile are separate but traceable.
- Six orchestrators and the Scenario Controller are represented consistently.
- P00 critical material gaps are closed before independent study.
- Administrative and learner-facing layers remain separate.
- Migration is reversible to the preserved RC3.7.0 snapshot.
