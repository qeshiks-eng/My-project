# Unified Cybersecurity Career Layer

The career layer is separate from learner-facing PXX content. It consumes verified project results and maps them to the job market.

## Per-role career profile

Every R01–R26 role has a traceable career profile containing:

- common job titles;
- market vocabulary;
- required technologies;
- required work products;
- supporting PXX projects;
- portfolio evidence;
- resume statements;
- interview questions;
- remaining gaps;
- readiness status.

## Traceability

```text
Role Rxx
  ↓
Role module across P00–P20
  ↓
LAB artifacts and evidence
  ↓
Public-safe portfolio items
  ↓
Career profile
  ↓
Vacancy, resume and interview mapping
```

## Readiness statuses

- `NOT_STARTED`
- `THEORY_IN_PROGRESS`
- `LAB_EVIDENCE_PARTIAL`
- `PORTFOLIO_READY`
- `APPLICATION_READY`
- `INTERVIEW_VALIDATED`

A role is not application-ready because its theory exists in the library. Readiness requires relevant evidence and the ability to explain the work.

## Market governance

Market analysis, vacancy data, location constraints, schedule filters and application strategy remain administrative data. They do not enter the core PXX learning text.

The current personal constraints remain part of the private career layer, not the public repository:

- no night shifts;
- bridge roles are acceptable when they do not destroy the study rhythm;
- laboratory work is described honestly as laboratory engineering practice;
- production experience is never invented.

## Resume rule

A resume statement must identify:

- what was built or changed;
- the environment and scope;
- the tools used;
- how the result was tested;
- what evidence exists;
- whether the work was laboratory or commercial.

## Portfolio rule

Career claims must link to one or more public-safe artifacts such as:

- architecture;
- code;
- tests;
- detection content;
- sanitized evidence;
- Run A/Run B comparison;
- incident case study;
- recovery report;
- assurance result.
