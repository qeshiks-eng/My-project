# v12 Migration Acceptance Checklist

The v12 candidate remains non-ACTIVE until every blocking item is verified.

## Source preservation

- [ ] Exact RC3.7.0 workbook bytes are mounted in the execution environment.
- [ ] SHA-256 equals `0949c3a07bcbe15acf723fd7fa04112038d9acd2703481838c0ad66858576702`.
- [ ] A byte-identical immutable backup exists.
- [ ] Every deleted or transformed source row has migration lineage.
- [ ] Legacy sources are marked, not silently erased.

## Program structure

- [x] P00–P20 taxonomy exists.
- [x] R01–R26 taxonomy exists.
- [x] Role, role module, career profile and responsibility are separated.
- [x] P19 and P20 are represented as specializations.
- [ ] Binary library contains exactly one learner-facing sheet per P00–P20.
- [ ] No unexpected formula or formatting drift exists.

## Learning model

- [x] Two-pass theory is canonical.
- [x] Complete primary reading applies to the current PXX.
- [x] Targeted rereading precedes practice.
- [x] Reference documentation is used on demand.
- [ ] Every migrated theory card has edition/scope/source/purpose/self-check/result fields.
- [ ] Russian primary route exists wherever available.

## Practice

- [x] Practice is real LAB engineering, not artificially weakened demonstration.
- [x] The only operational boundary is the user's isolated LAB.
- [x] Every practice action must retain an external source.
- [ ] Every migrated practice record has architecture, inputs, actions, negative tests, acceptance, evidence and cleanup.
- [ ] No practice source is an unbounded index when a specific lab or guide is required.

## Roles

- [x] P00–P18 require review of all R01–R26.
- [x] Applicable roles require real contributions.
- [x] Overview-only participation is forbidden.
- [x] Exceptional N/A requires technical rationale.
- [x] Implementer-only independent approval is forbidden.
- [ ] Every P00–P18 role record has theory, action, tool, artifact, test, evidence and handoff.

## Orchestration

- [x] Scenario Controller is separate from the domain orchestrators.
- [x] Shared Orchestration Core is defined.
- [x] Six first-class domain orchestrators are defined.
- [x] Domain orchestrators own process outcomes and may contain domain logic.
- [x] Decisions are deterministic by default.
- [x] AI authority is advisory only.
- [x] Scope checks cannot be disabled by CLI flags.
- [ ] Controller, Core and six orchestrators have executable P00 implementations.
- [ ] Contract schemas validate all P00 manifests and scenarios.

## P00 material readiness

- [x] Introductory Ubuntu/Nginx case is the P00 core.
- [x] Deep symlink/config-tampering case is preserved separately.
- [x] Run A and comparable Run B are specified.
- [x] All six orchestrators receive a minimal vertical slice.
- [ ] L02 network/snapshot route is source-complete.
- [ ] L05 Bash detection/testing route is source-complete and deterministic.
- [ ] L07 deploy/rollback/recovery route is source-complete.
- [ ] UTC/evidence and incident-record route is source-complete.
- [ ] Independent P00 material audit passes.
- [ ] Real P00 LAB execution passes Assurance.

## Evidence and portfolio

- [x] Private, machine-readable, human-readable and public-safe layers are separated.
- [x] Public repository excludes raw sensitive evidence.
- [x] Run A/Run B comparison requirements exist.
- [x] Portfolio claims are tied to evidence.
- [ ] Automated secret and public-safety checks pass.
- [ ] P00 public-safe case study is generated from real evidence.

## Stack

- [x] Tool registry schema exists.
- [x] P00 and internal orchestration seed entries exist.
- [ ] All P01–P20 assignments are normalized without loss.
- [ ] Product/component/specification aliases are deduplicated.
- [ ] Unique product and component counts are calculated.
- [ ] Exact execution versions and checksums are pinned.

## Activation

- [ ] Full row-level migration audit passes.
- [ ] Link and source-quality audit passes.
- [ ] Formula and visual audit passes.
- [ ] Repository contract validation passes.
- [ ] No blocking issue remains.
- [ ] Migration PR is reviewed.
- [ ] v12 is explicitly promoted from `MIGRATION_CANDIDATE` to `ACTIVE`.
