# PhantomLoop — v1 Client Contract

**Status**: Normative

## Abstract
PhantomLoop is a real-time visualization and decoder test harness. This document defines the minimum client-side requirements to consume PLSP v1 (PhantomLink streaming) reliably and to compute timing/latency metrics consistently.

## Responsibilities
A PhantomLoop-compatible client:
- **MUST** connect to PhantomLink’s binary stream endpoint (`/stream/binary/{session_code}`) unless debugging
- **MUST** decode MessagePack envelopes (`{type, data}`)
- **MUST** treat `sequence_number` as the primary ordering key
- **MUST** ignore unknown fields to remain forward-compatible

## Time and latency
- The incoming packet `data.timestamp` is Unix epoch seconds.
- Clients **MUST** compute latency using an epoch clock (e.g., `Date.now()`), not a monotonic clock.

Recommended computation:
- `latency_ms = max(0, Date.now() - (timestamp * 1000))`

## Metadata normalization
Clients **SHOULD** normalize metadata aliases to the canonical PLSP names:
- `channel_count → num_channels`
- `sampling_rate_hz → frequency_hz`
- `total_samples → total_packets`
- `trial_count → num_trials`

## Buffering
Clients **SHOULD** maintain a bounded ring buffer sized to at least 1 second of data (e.g., 40 packets at 40 Hz) to smooth renderer/decoder jitter.
