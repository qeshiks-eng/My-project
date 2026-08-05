# Evidence Model

## Principle

Evidence must show what happened, under which scope and versions, how the result was checked, and what conclusion follows.

A screenshot without commands, inputs, timestamps and context is supporting material, not sufficient evidence.

## Layers

### Private raw evidence

Stored outside the public repository:

- complete logs;
- full PCAP;
- memory and disk images;
- VM snapshots;
- malware samples;
- credentials and secrets;
- unsanitized configurations;
- sensitive findings.

### Machine-readable evidence

- `run-manifest.json`;
- `result.json`;
- `evidence-manifest.json`;
- `metrics.json`;
- `handoff.json`;
- structured test results;
- hashes and version records.

### Human-readable evidence

- `execution-report.md`;
- `incident-report.md`;
- `recovery-report.md`;
- `assurance-report.md`;
- `run-a-vs-run-b.md`.

### Public-safe evidence

- sanitized manifests;
- synthetic fixtures;
- safe configuration excerpts;
- architecture;
- tests;
- detection content;
- sanitized timelines;
- hashes where disclosure is safe;
- case-study documentation.

## Required record fields

Each significant action records:

- `run_id`;
- `project_id`;
- `scenario_id`;
- source and external practice reference;
- expected result;
- actual action or configuration;
- actual result;
- UTC start and finish;
- tool, module and orchestrator versions;
- command exit code or structured status;
- evidence references;
- hashes where applicable;
- conclusion;
- cleanup/rollback result;
- handoff.

## Integrity and authenticity

A hash confirms that the retained artifact did not change after hashing. It does not prove who created it or whether the source was trustworthy.

Evidence review must distinguish:

- integrity;
- authenticity;
- completeness;
- relevance;
- reproducibility.

## Run comparison

Run A and Run B comparison must document:

- equal or intentionally controlled inputs;
- version differences;
- time-window differences;
- expected result differences;
- security outcome;
- functional outcome;
- telemetry outcome;
- regression outcome;
- residual risk.

## Status truth

No evidence package may claim PASS until the Assurance Orchestrator has validated acceptance, completeness, recovery and comparison criteria.
