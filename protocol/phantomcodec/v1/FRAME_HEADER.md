# PhantomCodec v1 — Packet Header

## Overview
A PhantomCodec packet is:

- 8-byte fixed header
- followed by a strategy-specific payload

All multi-byte integers in the header are big-endian.

## Header layout (8 bytes)

```text
0               3 4   4 5       6 7
+----------------+-----+---------+---+
| Magic "PHDC"   | Ver | Channels| S |
+----------------+-----+---------+---+

Magic:   4 bytes 0x50 0x48 0x44 0x43
Ver:     1 byte  protocol version (0x01)
Channels:2 bytes unsigned big-endian channel count
S:       1 byte  strategy selector byte
```

## Strategy selector byte
The selector byte encodes:
- High 6 bits: `strategy_id`
- Low 2 bits: `rice_k` parameter (only meaningful for Rice strategy)

Formally:
- `strategy_id_raw = selector >> 2`
- `rice_k = selector & 0x03`

## Validation
Decoders **MUST** validate:
- Magic bytes exactly equal `PHDC`
- Version equals `0x01` for v1
- `strategy_id_raw` is a known value in the v1 registry

On validation failure, decoders **MUST** return an explicit error and **MUST NOT** produce output data.
