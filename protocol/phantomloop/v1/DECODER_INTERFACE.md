# PhantomLoop — v1 Decoder Interface

**Status**: Normative

## Purpose
This document standardizes the minimal in-process decoder interface PhantomLoop uses to run decoders (JavaScript or TensorFlow.js) against PLSP v1 packets.

## Inputs
Decoders operate on a per-packet basis with optional short history.

### DecoderInput
A decoder input object **MUST** contain:

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `spikes` | array[number] | yes | Spike counts per channel (typically integers) |
| `kinematics` | object | yes | Ground truth kinematics (may be partial) |
| `history` | array[DecoderOutput] | yes | Recent outputs (bounded, e.g. last 40) |

`kinematics` **MUST** contain:
- `x`, `y`, `vx`, `vy` (numbers; may be `null` if not present upstream)

## Outputs
### DecoderOutput
A decoder output object **MUST** contain:

| Field | Type | Required | Notes |
|---|---:|:---:|---|
| `x` | number | yes | Estimated cursor x |
| `y` | number | yes | Estimated cursor y |
| `vx` | number | yes | Estimated velocity x |
| `vy` | number | yes | Estimated velocity y |
| `latency` | number | yes | Decoder compute latency in milliseconds |

## Execution model
- Implementations **MAY** be synchronous or asynchronous.
- PhantomLoop **MUST** avoid concurrent execution on multiple packets for a single decoder instance.
- PhantomLoop **SHOULD** de-duplicate packets by `sequence_number`.

## State reset
- On decoder switch, PhantomLoop **MUST** reset decoder state/history.
