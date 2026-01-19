# Versioning

PhantomSpecs versions **specifications**, not implementations.

## Spec version format

Each spec is versioned as `vMAJOR.MINOR`.

- **MAJOR**: breaking changes to fields, semantics, units, requiredness, or encodings.
- **MINOR**: additive-only changes (new optional fields, new message types, new strategy IDs).

Patch-level changes are handled in Git history and `CHANGELOG.md` but do not change on-wire formats.

## Backward/forward compatibility rules

- Readers (clients/servers) **MUST ignore unknown fields** they do not understand.
- Writers **MUST NOT remove or rename fields** within a major version.
- Writers **MAY add new optional fields** within a minor version.
- If a breaking rename is needed, it **MUST** be introduced as:
  1) Add new field (minor)
  2) Deprecate old field (documented)
  3) Remove old field (next major)

## Where the version lives

- For PhantomLink streaming, the protocol version is carried in the **metadata** message.
- For PhantomCodec framing, the version is carried in the **packet header**.
