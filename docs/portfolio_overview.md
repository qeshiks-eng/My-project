# Portfolio Overview

## Purpose

This repository is the public-safe projection of work performed in the Enterprise Cybersecurity Program.

The portfolio is not a collection of course notes or screenshots. It must show a reproducible engineering chain:

`problem → architecture → baseline → Run A → telemetry → investigation → root cause → remediation → Run B → recovery → assurance`

## Portfolio architecture

The mature portfolio contains:

- one Enterprise Cybersecurity Lab repository;
- P00–P20 project case studies;
- ECP Scenario Controller;
- Orchestration Core;
- Delivery, Defense, Attack, Investigation, Recovery and Assurance orchestrators;
- domain modules and adapters;
- architecture and ADR;
- tests and detection content;
- public-safe evidence indexes;
- selected flagship cases;
- integration capstone P18;
- specialization cases P19 and P20.

## Project page standard

Each mature PXX page should contain:

1. problem and scope;
2. architecture and trust boundaries;
3. assets and threat model;
4. primary theory route and practice sources;
5. baseline and versions;
6. Run A;
7. telemetry and detection;
8. investigation and timeline;
9. root cause;
10. remediation;
11. comparable Run B;
12. QA and regression;
13. recovery and rollback;
14. metrics;
15. Assurance result;
16. limitations and residual risk;
17. public artifacts.

## Role evidence

Roles are proven by artifacts rather than labels.

Examples:

- GRC: risk and control mapping;
- Architecture: C4, DFD and ADR;
- Network/Platform/AppSec/Identity: configurations and tests;
- Attack: scoped scenarios, frozen inputs and cleanup evidence;
- Detection: rules, fixtures and regression tests;
- SOC/IR/DFIR/Hunting: triage, timeline, hypotheses and findings;
- Recovery: verified backups, restore and RTO/RPO;
- QA/Assurance: acceptance, negative and regression tests;
- DevSecOps/Automation: delivery manifests, code and provenance;
- Documentation/Portfolio: traceable public-safe release.

## Evidence layers

### Private raw evidence

Stored outside the public repository:

- full logs;
- PCAP;
- disk and memory images;
- VM snapshots;
- malware samples;
- secrets and credentials;
- unsanitized configurations;
- sensitive findings.

### Machine-readable public-safe evidence

- sanitized run manifest;
- evidence index;
- result and metrics;
- hashes of retained private artifacts where disclosure is safe;
- handoff records;
- schema-valid fixtures.

### Human-readable evidence

- execution report;
- incident report;
- recovery report;
- Assurance report;
- Run A versus Run B comparison.

## Employer navigation

The portfolio should support three review depths:

- approximately two minutes: repository overview and flagship outcomes;
- approximately ten minutes: one complete case study;
- deep review: code, tests, manifests, architecture and evidence lineage.

## Public safety rule

Public artifacts must be sanitized and reproducible without exposing dangerous or sensitive material.

Use:

- synthetic fixtures;
- sanitized excerpts;
- defensive runbooks;
- detection rules;
- test code;
- safe configurations;
- architecture diagrams;
- controlled demonstrations in the user's local LAB.

## Status truth

A planned artifact is not presented as implemented. An implemented artifact is not presented as LAB-validated. A LAB result is not presented as PASS until Assurance criteria are satisfied.

Laboratory engineering practice is described honestly as laboratory work, not as commercial production experience.
