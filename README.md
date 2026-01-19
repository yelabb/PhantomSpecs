# PhantomSpecs

PhantomSpecs is the normative specification repository for the **Phantom Suite**:
- PhantomLink (Python streaming server)
- PhantomLoop (TypeScript/React visualization client)
- PhantomCore (C++ decoding/processing library)
- PhantomCodec (Rust codec + wire framing)

This repo exists to prevent protocol and data-model drift across implementations.

## What this repo contains

- **Protocol specs** (human-readable, normative): `protocol/**/v1/*.md`
- **Schemas** (machine-readable): `schemas/**/v1/*`
- **Vectors** (golden examples to test compatibility): `vectors/**/v1/*`

## How to use

- Implementations MUST follow the **normative** documents in `protocol/`.
- Implementations SHOULD validate inputs/outputs against `schemas/`.
- Implementations SHOULD include CI tests that round-trip or validate `vectors/`.

## Normative language

This repository uses RFC 2119 keywords: **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**.
