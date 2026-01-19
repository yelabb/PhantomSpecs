# PhantomCodec — v1 Framing and Strategy Registry

**Status**: Normative

## Abstract
PhantomCodec defines a compact binary framing and a set of compression strategies for neural vectors (e.g., spike counts or voltage samples). This spec defines the on-wire packet header and the strategy ID registry used by PhantomCodec v1.

## Scope
This v1 spec standardizes:
- Packet header bytes (magic, version, channel count, strategy selector)
- Strategy identifiers and their meaning

This spec does **not** standardize:
- Transport (WebSocket/UDP/etc.)
- Session semantics, timestamps, or envelopes (handled by PLSP)
- Implementation-specific APIs (e.g., function signatures, memory management)

## Normative language
The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

## Implementation notes
The reference Rust implementation (`PhantomCodec` crate) provides a `#![no_std]` compatible API. Implementors of other languages should follow the wire format described in [FRAME_HEADER.md](FRAME_HEADER.md) and [STRATEGIES.md](STRATEGIES.md).

Key implementation considerations:
- All multi-byte integers in the header are **big-endian**
- The payload format is strategy-specific and defined per strategy
- Decoders **MUST** validate magic bytes and version before processing
