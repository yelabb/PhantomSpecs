# PhantomSpecs

PhantomSpecs is the normative specification repository for the **Phantom Stack**:
- **PhantomX** (Python ML research platform): https://github.com/yelabb/PhantomX
- **PhantomLink** (Python streaming server): https://github.com/yelabb/PhantomLink
- **PhantomLoop** (TypeScript/React visualization client): https://github.com/yelabb/PhantomLoop
- **PhantomCore** (C++ decoding/processing library): https://github.com/yelabb/PhantomCore
- **PhantomZip** (Rust codec + wire framing): https://github.com/yelabb/PhantomZip

This repository:
- **PhantomSpecs**: https://github.com/yelabb/PhantomSpecs

This repo exists to prevent protocol and data-model drift across implementations.

## What this repo contains

- **Protocol specs** (human-readable, normative): `protocol/**/v1/*.md`
- **Schemas** (machine-readable): `schemas/**/v1/*`
- **Vectors** (golden examples to test compatibility): `vectors/**/v1/*`

See the index of available specs in [SPEC_INDEX.md](SPEC_INDEX.md).

## How to use

- Implementations MUST follow the **normative** documents in `protocol/`.
- Implementations SHOULD validate inputs/outputs against `schemas/`.
- Implementations SHOULD include CI tests that round-trip or validate `vectors/`.

### Validate locally
From this repo root:

- Install tooling deps: `python -m pip install -r tooling/requirements.txt`
- Run validation: `python tooling/validate_vectors.py`

## Normative language

This repository uses RFC 2119 keywords: **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, **MAY**.
