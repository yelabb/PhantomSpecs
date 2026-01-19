# PhantomCore — v1 Stream Compatibility

**Status**: Normative

## Abstract
PhantomCore provides high-performance native components for consuming PhantomLink streams and running decoding/analytics. This document defines PhantomCore’s required compatibility with PLSP v1.

## Key requirement
A PhantomCore client **MUST** decode PhantomLink binary stream messages as MessagePack maps with the PLSP v1 envelope:

- `{ "type": "metadata", "data": { ... } }`
- `{ "type": "data", "data": { ... } }`

Any proprietary fixed-header framing (e.g., magic bytes) is **not** part of PLSP v1.

## Backward/forward compatibility
- PhantomCore consumers **MUST** ignore unknown fields.
- PhantomCore **SHOULD** accept metadata alias field names as described in PLSP v1.
