# Program Stack Registry

The learning library currently contains hundreds of tool assignments. An assignment is not the same as a unique product.

A single product may appear:

- in multiple projects;
- for multiple roles;
- through different components;
- at different depth levels;
- with different adapters and version pins.

## Required registry files

```text
stack/
├── registry.yaml
├── aliases.yaml
├── project-mapping.yaml
├── registry.schema.yaml
└── versions.lock
```

## Depth levels

- `CORE`: studied and used confidently; key behavior and failure modes are tested.
- `WORKING`: used independently with documentation.
- `INTEGRATED`: connected through an adapter; only the required operational scope is studied.
- `REFERENCE`: alternative, historical or supplementary product.

## Product versus component

Examples:

- Wireshark is a product; `tshark` and `capinfos` are components.
- systemd is a product family; `systemctl` and `journalctl` are operational components.
- Kubernetes is a platform; `kubectl` is a client component.
- Ansible may include `ansible-core`, collections, Molecule and Testinfra.

Aliases must not create multiple fake unique products.

## Required registry fields

- stable `tool_id`;
- canonical name;
- category;
- product/components relationship;
- license and cost model;
- availability;
- version policy;
- official manual;
- project mappings;
- role mappings;
- orchestrator mappings;
- depth level;
- evidence of actual use;
- status.

## Version policy

The library may define the intended version policy, but the exact version and checksum are pinned immediately before real execution and stored in `versions.lock` and the run manifest.

Rolling documentation must have a check date. A prerelease cannot silently replace a stable core route.

## Status truth

- `CATALOGUED` means the product exists in the registry.
- `ASSIGNED` means it is mapped to a project.
- `INSTALLED` means installation evidence exists.
- `USED` means a real LAB action exists.
- `VALIDATED` means tests and evidence confirm the required behavior.

A catalog entry does not prove practical proficiency.
