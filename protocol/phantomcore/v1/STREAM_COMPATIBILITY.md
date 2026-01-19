# PhantomCore — v1 PLSP Binary Decoding

## Message framing
- Each WebSocket message payload is a complete MessagePack object.
- The decoded object **MUST** be a map containing `type` (string) and `data` (map).

## Mapping to native structs
PhantomCore implementations **SHOULD** map PLSP payloads into strongly typed structs.

### Recommended native model (conceptual)
- `Metadata`
  - `dataset: string`
  - `total_packets: uint64`
  - `frequency_hz: uint32`
  - `num_channels: uint32`
  - `duration_seconds: double`
  - `num_trials: uint32`

- `StreamPacket`
  - `timestamp: double` (Unix epoch seconds)
  - `sequence_number: uint64`
  - `spikes.channel_ids: vector<int32>`
  - `spikes.spike_counts: vector<int32>`
  - `spikes.bin_size_ms: double`
  - `kinematics.{vx,vy,x?,y?}: double`
  - `intention.{target_id?,target_x?,target_y?,distance_to_target?}: double/int`
  - `trial_id?: int`
  - `trial_time_ms?: double`

## Validation rules
On `data` messages, PhantomCore **MUST** validate:
- `channel_ids.length == spike_counts.length`
- `spike_counts.length == num_channels` (if metadata has been received)

If validation fails, PhantomCore **SHOULD** drop the packet and surface an error counter rather than terminating the connection.

## Latency
If PhantomCore computes network latency from `timestamp`, it **MUST** use an epoch clock source.

## Control
Playback control is HTTP in v1 (see PLSP transport). PhantomCore **MUST NOT** assume WebSocket control messages are supported.
