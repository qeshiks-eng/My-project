# Projects P00–P20

Each project is a versioned extension of one evolving Enterprise Cybersecurity Lab.

## Project list

| ID | Project |
|---|---|
| P00 | Start, engineering method and evidence discipline |
| P01 | Packet analysis and network baseline |
| P02 | DNS, DHCP, routing, NTP and SSH |
| P03 | Segmentation, VLAN, policy and failover |
| P04 | Network telemetry, IDS, NSM and evidence handling |
| P05 | Linux hardening and host security |
| P06 | Windows Security, DFIR and timeline |
| P07 | Cryptographic primitives and misuse |
| P08 | Data protection and key lifecycle |
| P09 | Signatures, public-key trust and PQC |
| P10 | PKI, TLS, mTLS and workload identity |
| P11 | Asset inventory, telemetry and data platform |
| P12 | Controlled adversary operations |
| P13 | Detection engineering and threat hunting |
| P14 | Enterprise network security architecture |
| P15 | DevSecOps, IaC and software supply chain |
| P16 | Enterprise Identity and Active Directory |
| P17 | Kubernetes and GitOps security common core |
| P18 | Integration capstone, resilience and assurance |
| P19 | Threat research, malware analysis and reverse engineering |
| P20 | Cloud-Native Security and Platform Security |

## Required PXX package

```text
projects/pXX/
├── README.md
├── technical-manifest.yaml
├── architecture/
│   ├── c4/
│   ├── dfd/
│   └── adr/
├── theory-route.md
├── practice-sources.md
├── roles/
├── scenarios/
│   ├── baseline.yaml
│   ├── run-a.yaml
│   └── run-b.yaml
├── modules/
├── tests/
├── runbooks/
├── evidence-index/
├── reports/
└── public/
```

Raw evidence is stored outside the public repository.

## Mandatory project cycle

1. Project scope and architecture.
2. First-pass complete theory route.
3. Targeted rereading before each technical action.
4. Delivery baseline.
5. Defense baseline and telemetry.
6. Assurance readiness gate.
7. Verified recovery point.
8. Run A.
9. Investigation and root cause.
10. Remediation.
11. Delivery of the fix.
12. Functional and regression verification.
13. Comparable Run B.
14. Investigation of Run B.
15. Recovery/rollback drill.
16. Assurance final gate.
17. Public-safe portfolio release.

## Role coverage

For P00–P18:

- every R01–R26 role is explicitly reviewed;
- applicable roles perform real work and produce evidence;
- overview-only participation is forbidden;
- exceptional `N/A` requires a written technical rationale;
- the implementer cannot independently approve the same result.

P19 and P20 may use specialized role coverage.

## Technical manifest

The manifest contains only execution data required by the LAB and orchestrators:

- project and scenario identifiers;
- assets and inventory;
- scope and allowlists;
- threat and control objectives;
- inputs and expected outputs;
- workflow;
- test and evidence requirements;
- recovery requirements;
- PASS criteria.

Program versions, audits, migration history and market analysis remain in `governance/`.

## Status truth

Project status is reported using separate fields:

- `DESIGNED`;
- `IMPLEMENTED`;
- `LAB_VALIDATED`;
- `ASSURANCE_STATUS`.

A project is complete only when `ASSURANCE_STATUS=PASS`.
