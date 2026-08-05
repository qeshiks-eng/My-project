# Safety and Scope

## Core rule

Practice is performed as real engineering work, with one operational boundary:

> All actions are restricted to the user's own isolated Enterprise Cybersecurity Lab.

The LAB boundary does not artificially weaken attack, defense, investigation, recovery, QA or automation. It prevents the work from reaching systems, data or people outside the authorized laboratory.

## Allowed environments

- owned local virtual machines;
- isolated VMware or validated EVE-NG networks;
- intentionally created training environments;
- owned services and applications;
- synthetic datasets;
- sanitized sample data;
- intentionally acquired training malware stored and handled in an isolated analysis environment;
- historical vulnerabilities and former zero-days reproduced only inside the LAB.

## Required scope controls

Every scenario must define:

- allowed hosts;
- allowed networks;
- allowed services and accounts;
- permitted techniques;
- prohibited actions;
- time window;
- emergency stop;
- cleanup and recovery requirements.

The Scenario Controller and orchestrators must reject targets outside the approved inventory. Scope checks cannot be disabled by a command-line flag.

## Prohibited actions

- unauthorized access to third-party systems;
- scanning or attacking public targets;
- credential theft from real users;
- persistence or evasion on production systems;
- use of real production data;
- collection or publication of real secrets;
- publication of private keys;
- publication of personal data;
- publication of production traffic or logs;
- transfer of offensive scenarios outside the approved LAB scope;
- arbitrary command execution exposed as an unrestricted orchestration interface.

## Artifact policy

Do not commit:

- passwords;
- tokens;
- API keys;
- private keys;
- real credentials;
- full unsanitized PCAP;
- production logs;
- personal data;
- malware samples;
- VM snapshots;
- memory or disk images;
- sensitive host inventories;
- raw private evidence;
- temporary runtime files.

## Evidence storage

### Private evidence vault

May contain raw logs, full PCAP, forensic images, snapshots, malware and unsanitized artifacts. It remains local, access-controlled and excluded from the public repository.

### Public repository

May contain:

- sanitized evidence indexes;
- hashes where disclosure is safe;
- synthetic fixtures;
- sanitized excerpts;
- architecture;
- source code;
- detection content;
- tests;
- safe configuration examples;
- public-safe case studies.

## Technical interview demonstration

A deeper local LAB demonstration may be shown to an authorized technical interviewer. The demonstration remains controlled and does not grant access to secrets, unsafe artifacts, third-party data or unrestricted offensive capability.

## AI boundary

AI may assist with summarization, classification, hypothesis generation or report drafting. AI cannot:

- expand scope;
- add external targets;
- execute arbitrary commands;
- change PASS criteria;
- destroy or alter evidence;
- trigger irreversible recovery actions without approval;
- declare root cause without supporting evidence.
