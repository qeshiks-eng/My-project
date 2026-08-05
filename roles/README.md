# Role Modules R01–R26

## Terminology

### Role

A professional function performed inside a project.

### Role module

The complete learning and engineering representation of a role across P00–P20. Each role module contains:

- competency map;
- first-pass theory route;
- targeted theory route;
- external practice sources;
- tools and depth level;
- project actions;
- inputs and handoffs;
- artifacts;
- tests;
- evidence;
- career profile mapping.

### Career profile

The translation of proven role results into job titles, vacancy requirements, resume statements, portfolio evidence and interview preparation.

### Responsibility

Reviewer, approver, evidence owner, recovery owner and handoff owner are responsibilities. They are not separate career roles.

## Registry

| ID | Role |
|---|---|
| R01 | Governance, Risk and Compliance |
| R02 | Security Architecture |
| R03 | Network Security |
| R04 | Platform and Systems Security |
| R05 | Endpoint Security |
| R06 | Application Security |
| R07 | Cloud and Container Security |
| R08 | Identity Security |
| R09 | Data Security and Cryptography |
| R10 | Vulnerability Management |
| R11 | Threat Modeling |
| R12 | Threat Intelligence |
| R13 | Adversary Emulation and Red Team |
| R14 | Detection Engineering |
| R15 | SOC and Monitoring |
| R16 | Incident Response |
| R17 | Digital Forensics and Incident Response |
| R18 | Threat Hunting |
| R19 | Malware and Payload Analysis |
| R20 | QA and Security QA |
| R21 | DevSecOps and Supply Chain Security |
| R22 | Security Automation |
| R23 | Telemetry and Data Engineering |
| R24 | Resilience and Recovery |
| R25 | Documentation and Knowledge Engineering |
| R26 | Program and Portfolio Engineering |

## P00–P18 coverage rule

Every project explicitly reviews all R01–R26.

For every applicable role, the project must contain:

1. defined professional objective;
2. theory sufficient for the objective;
3. one or more external practice sources;
4. actual LAB action;
5. tool route;
6. versioned artifact;
7. positive and negative verification;
8. evidence;
9. handoff or review result.

A role is not complete because it appears in a spreadsheet, diagram or paragraph.

`N/A` is exceptional and requires a technical rationale showing why the role has no meaningful action in the bounded project scope. It cannot be used merely to reduce workload.

## Separation of duties

- The implementer cannot independently issue final PASS for the same artifact.
- Reviewer and approver are recorded separately where practical.
- Evidence ownership, recovery ownership and handoff ownership must remain traceable.
- A single learner may perform multiple roles sequentially, but the artifacts must preserve the logical independence of implementation and verification.

## Orchestrator participation

Orchestrators are cross-role processes, not career roles.

Typical leading roles:

- Delivery: R21 and R22;
- Defense: R03, R04, R05, R06, R07, R08 and R21;
- Attack: R13 with R06, R11, R12 and R19;
- Investigation: R15, R16, R17, R18 and R23;
- Recovery: R24 with R16, R04, R08, R09 and R21;
- Assurance: R20 and R26 with architecture, GRC and domain owners.

## Evidence of role competence

Role competence is proven by artifacts, not labels. Examples:

- architecture decisions;
- configurations;
- detection rules;
- test suites;
- PCAP and log analyses;
- timelines;
- incident records;
- remediation diffs;
- recovery reports;
- automation code;
- public-safe case studies.
