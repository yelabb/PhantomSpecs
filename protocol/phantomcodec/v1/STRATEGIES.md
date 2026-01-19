# PhantomCodec v1 — Strategy Registry

## Strategy IDs
The v1 registry defines the following `strategy_id` values:

| ID (decimal) | ID (hex) | Name | Lossless | Intended data |
|---:|---:|---|:---:|---|
| 0 | 0x00 | DeltaVarint | yes | Spike counts (unsigned / small deltas) |
| 1 | 0x01 | Rice | yes | Signed values (e.g., voltage deltas) |
| 2 | 0x02 | Packed4 | no | Low-latency lossy quantization |
| 3 | 0x03 | FixedWidth | yes | Block packing (PFOR-like) |

## Rice parameter `k`
For the Rice strategy (ID = 1), the header provides a 2-bit parameter:
- `k` is encoded in the low 2 bits of the selector byte.
- Valid range: 0–3.

For non-Rice strategies, decoders **MUST** ignore `rice_k`.

## Extensibility
- New strategies **MUST** be introduced by bumping PhantomCodec protocol version and allocating new IDs.
- Decoders **MUST** reject unknown strategy IDs for a given version.
