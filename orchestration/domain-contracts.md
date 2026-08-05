# Domain Orchestrator Contracts

All orchestrators use the shared `run_id`, versioned manifests, deterministic state transitions and explicit evidence handoffs.

## Delivery Orchestrator

### Owns

- source and commit selection;
- dependency and build checks;
- configuration rendering;
- deployment;
- post-deployment verification;
- rollback preparation and execution;
- delivery evidence.

### Required inputs

- project technical manifest;
- source revision;
- inventory;
- version lock;
- deployment profile;
- rollback target;
- approved change record.

### Required outputs

- `delivery-plan.json`;
- `build-result.json` where applicable;
- `deployment-result.json`;
- `applied-diff.json`;
- `post-deploy-checks.json`;
- `rollback-result.json` when invoked;
- handoff to Defense and Assurance.

## Defense Orchestrator

### Owns

- desired security state;
- hardening and access controls;
- telemetry baseline;
- detection deployment;
- policy enforcement;
- control verification;
- defensive rollback.

### Required inputs

- architecture and threat model;
- golden baseline;
- inventory and allowlists;
- approved controls;
- telemetry requirements;
- recovery objective.

### Required outputs

- `defense-plan.json`;
- `control-state-before.json`;
- `control-state-after.json`;
- `telemetry-readiness.json`;
- `control-tests.json`;
- handoff to Attack, Investigation and Assurance.

## Attack Orchestrator

### Owns

- owned-LAB scope validation;
- attack scenario and frozen inputs;
- realistic execution within scope;
- attacker-side telemetry;
- stop conditions;
- Run A/Run B comparability;
- cleanup and orphan checks.

### Required inputs

- signed/approved scope;
- ownership proof;
- scenario manifest;
- target allowlist;
- permitted techniques;
- frozen variables;
- emergency stop and cleanup plan.

### Required outputs

- `attack-plan.json`;
- `scope-validation.json`;
- `execution-log.jsonl`;
- `attacker-observations.json`;
- `cleanup-result.json`;
- handoff to Investigation and Assurance.

## Investigation Orchestrator

### Owns

- evidence ingestion;
- integrity verification;
- PCAP, log and host-artifact analysis;
- UTC normalization;
- correlation and timeline;
- facts, hypotheses and confidence;
- findings and incident export.

### Required inputs

- raw evidence manifest;
- run context;
- hashes;
- time synchronization proof;
- case hypothesis boundary;
- parsing and correlation profiles.

### Required outputs

- `ingestion-result.json`;
- `integrity-checks.json`;
- `timeline.json` or `timeline.csv`;
- `hypothesis-log.md`;
- `findings.json`;
- `incident-report.md`;
- handoff to Defense, Recovery and Assurance.

## Recovery Orchestrator

### Owns

- backup and snapshot policy;
- recovery-point creation;
- backup integrity;
- restore and rollback;
- startup order;
- service and functional health;
- RTO/RPO measurement;
- cleanup of temporary recovery assets.

### Required inputs

- recovery objective;
- protected datasets;
- backup target;
- retention rule;
- service dependency order;
- health checks;
- previous recovery manifest.

### Required outputs

- `recovery-plan.json`;
- `backup-manifest.json`;
- `integrity-result.json`;
- `restore-result.json`;
- `service-health.json`;
- `rto-rpo.json`;
- `cleanup-result.json`;
- handoff to Delivery and Assurance.

## Assurance Orchestrator

### Owns

- prerequisites and acceptance criteria;
- functional and security tests;
- negative and malformed inputs;
- regression and idempotence;
- Run A/Run B comparison;
- evidence and handoff validation;
- recovery validation;
- final gate decision.

### Required inputs

- project technical manifest;
- test strategy;
- expected results;
- all orchestrator handoffs;
- evidence manifests;
- Run A and Run B contexts;
- recovery report.

### Required outputs

- `readiness-gate.json`;
- `functional-tests.json`;
- `security-tests.json`;
- `regression-tests.json`;
- `run-comparison.json`;
- `evidence-validation.json`;
- `assurance-report.md`;
- final status: `PASS`, `FAIL`, `BLOCKED` or `NEEDS_REVIEW`.

## Shared prohibitions

No orchestrator contract may expose:

- `--disable-scope-check`;
- `--allow-external-targets`;
- unrestricted `--shell`;
- plaintext secrets in CLI history;
- silent evidence deletion;
- undocumented destructive fallback;
- AI authority to approve, expand scope or execute arbitrary actions.
