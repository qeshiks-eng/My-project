# Semantic Rebuild Stage 2 · Source Normalization

- Date: 2026-08-04
- Status: `MIGRATION_CANDIDATE`
- Parent: `v12.0_SEMANTIC_REBUILD_STAGE1`
- Output: `12_LIBRARY_SCHEMA_P00-P20_v12.0_SEMANTIC_REBUILD_STAGE2_SOURCE_NORMALIZED.xlsx`
- Output SHA-256: `052ea23a75a1f282176be9581125eb980a4fa1186529c59e45b9d75341962bbb`

## Completed

- Preserved exactly 21 learner-facing sheets P00–P20.
- Preserved P00–P18 explicit role coverage R01–R26.
- Added 315 explicit source fields without deleting legacy content.
- Reduced non-empty theory cells without URL from 168 to 0.
- Kept non-empty practice cells without URL at 0.
- Reduced non-empty tool cells without guide URL from 147 to 0.
- Added five P00 material-repair blocks:
  - L02 network, trust boundaries and diagnostics;
  - L02 VMware snapshot/copy and recovery point;
  - L05 Bash detector engineering with ShellCheck and Bats;
  - L06 UTC, integrity and incident evidence;
  - L07 deployment, rollback, restore and acceptance.
- Added Russian primary routes for Git, network fundamentals, Nginx, Bash and journalctl where suitable.
- Retained original/official English sources where required for technical accuracy.
- Kept administrative audit data outside the learner-facing library.

## P00 source set

- Pro Git Russian edition and Russian Git command reference.
- SDSM / Linkmeup plus current Ubuntu Server networking documentation.
- Nginx Russian documentation and beginner guide.
- Debian Russian Bash manpage plus the GNU Bash manual.
- ShellCheck and bats-core documentation.
- Russian journalctl guide plus the systemd journalctl reference.
- Broadcom VMware Workstation knowledge-base material for VM copy and snapshot behavior.
- Ansible check/diff documentation.
- restic backup, check and restore documentation.
- RFC 3339 and NIST SP 800-61 Rev. 3 for timestamps and incident evidence.

## Audit result

```text
Project sheets:                21
P00-P18 with R01-R26:          19/19
Theory cells without URL:      0
Practice cells without URL:    0
Tool cells without URL:        0
Formula errors:                0
LAB execution:                 NOT_STARTED
Activation:                    MIGRATION_CANDIDATE
```

## Limitations

- URL presence is structurally complete, but a live reachability, edition, scope and source-quality audit is still required for inherited links.
- P15–P20 remain semantic role-level rebuilds rather than byte-identical legacy hydration.
- The five P00 repair blocks define a complete route but have not yet been executed in the LAB.
- Source cards do not prove installation, use, validation or professional proficiency.

## Next gate

1. Live URL and source-quality audit.
2. Duplicate and semantic-scope normalization.
3. Global product/component/tool registry normalization.
4. Independent P00 sequence and prerequisite review.
5. Repository migration review.
6. Real P00 LAB execution and Assurance decision.
