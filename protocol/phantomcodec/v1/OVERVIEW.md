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

## Normative language
The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.
