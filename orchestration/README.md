# ECP Orchestration Platform

## Architecture

```text
Human operator
      │
      ▼
ECP Scenario Controller
      │
      ▼
Orchestration Core
      │
      ├── Delivery Orchestrator
      ├── Defense Orchestrator
      ├── Attack Orchestrator
      ├── Investigation Orchestrator
      ├── Recovery Orchestrator
      └── Assurance Orchestrator
              │
              ▼
      Domain modules and adapters
              │
              ▼
      External tools and Enterprise LAB
```

The Scenario Controller coordinates complete PXX workflows. It is not a seventh domain orchestrator.

## Shared lifecycle

Every orchestrator supports the same high-level lifecycle:

`validate → plan → prepare → execute → observe → verify → collect evidence → report → cleanup/rollback`

Common states:

- `CREATED`
- `VALIDATED`
- `PLANNED`
- `PREPARED`
- `RUNNING`
- `VERIFYING`
- `SUCCEEDED`
- `FAILED`
- `BLOCKED`
- `NEEDS_REVIEW`
- `ROLLED_BACK`
- `CLEANED`

## Common run context

Every action is tied to a single `run_id` and records:

- `project_id`;
- `scenario_id`;
- `phase`;
- `environment`;
- `operator`;
- scope and allowlists;
- versions and checksums;
- inputs;
- step results;
- exit codes and errors;
- evidence references;
- cleanup or rollback result;
- final status;
- handoff.

## Commands

Recommended CLI form:

```bash
ecp scenario execute --file scenarios/p00/run-a.yaml

ecp delivery deploy --manifest projects/p00/technical-manifest.yaml
ecp defense apply --baseline projects/p00/defense-baseline.yaml
ecp attack execute --scenario scenarios/p00/run-a.yaml
ecp investigation pcap analyze --input /private-evidence/p00/run-a/traffic.pcapng
ecp recovery backup create --target web01 --dataset nginx-config --verify
ecp assurance gate --project P00 --run-id p00-run-a-001
```

The public CLI accepts structured intent. Arbitrary shell execution is not a supported orchestration contract.

## Inputs

Orchestrators may receive:

- commands and subcommands;
- boolean flags;
- typed parameters;
- configuration files;
- inventory;
- profiles;
- scenario variables;
- namespaced module options;
- secret references;
- stdin streams where appropriate.

Safety and scope policies cannot be disabled by a CLI flag.

## Domain responsibility

### Delivery

Owns build, dependency checks, SBOM/provenance, deployment, post-deployment verification and rollback.

### Defense

Owns baselines, hardening, access controls, telemetry, detection deployment, policy enforcement and control verification.

### Attack

Owns controlled adversary activity, realistic attack paths, Run A/Run B comparability, telemetry markers, stop conditions and cleanup inside the LAB scope.

### Investigation

Owns evidence ingestion, PCAP/log/host analysis, timeline, correlation, hypotheses, findings and incident export.

### Recovery

Owns backup, snapshots, integrity checks, restore, rollback, service health and RTO/RPO evidence.

### Assurance

Owns acceptance, functional and security tests, negative and malformed inputs, regression, idempotence, Run A/Run B comparison, evidence completeness and final gate status.

## Decision model

Mandatory decisions are deterministic and auditable:

- state transitions;
- policy checks;
- thresholds;
- typed validation;
- known failure paths;
- deterministic heuristics;
- explicit approval gates.

Unknown or ambiguous cases become `NEEDS_REVIEW`.

An optional AI adapter may summarize, classify or propose hypotheses. It cannot control scope, issue PASS, alter evidence, run arbitrary commands or make irreversible changes without an approved deterministic path.

## Handoff model

Orchestrators communicate through versioned manifests, not by importing each other's internal business logic.

A full PXX flow may be:

1. Delivery deploys baseline.
2. Defense applies controls and telemetry.
3. Assurance validates readiness.
4. Recovery creates a verified recovery point.
5. Attack performs Run A.
6. Investigation analyzes the evidence.
7. Assurance records the original result.
8. Recovery restores where required.
9. Defense applies remediation.
10. Delivery deploys the fix.
11. Assurance validates normal function.
12. Attack performs comparable Run B.
13. Investigation confirms telemetry and impact.
14. Recovery proves rollback/restore.
15. Assurance issues PASS, FAIL, BLOCKED or NEEDS_REVIEW.

The flow may branch when Investigation requests more evidence, Assurance rejects a result, or Recovery blocks an unsafe next step.

## Implementation policy

- P00 implements a minimal real vertical slice of all six orchestrators and the Controller.
- P01–P17 add adapters and deeper domain capabilities.
- P18 integrates the entire lifecycle.
- P19 and P20 add specialization-specific adapters.
- Reusable low-level work stays in modules or mature external tools.
- Orchestrators remain responsible for end-to-end results and evidence.
