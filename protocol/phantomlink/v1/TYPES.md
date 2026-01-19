# PLSP v1 — Message Envelope and Types

## Encoding
### JSON endpoint
- Each WebSocket message is a JSON object.

### Binary endpoint
- Each WebSocket message is a MessagePack-encoded map.
- MessagePack encoding **MUST** use standard types; map keys are UTF-8 strings.

## Envelope (common)
Every message (JSON or MessagePack) is an object with:

| Field | Type | Required | Description |
|---|---:|:---:|---|
| `type` | string | yes | Message discriminator: `"metadata"` or `"data"` |
| `data` | object | yes | Payload associated with `type` |

Consumers **MUST** ignore unknown top-level fields.

### Note: session info
The JSON `metadata` message in the current implementation may include an extra `session` object (e.g., `{code, url}`). Binary messages do not.
- Consumers **MUST NOT** require `session`.

## `metadata` payload
Canonical metadata fields (aligned to PhantomLink `StreamMetadata`):

| Field | Type | Required | Semantics |
|---|---:|:---:|---|
| `dataset` | string | yes | Dataset identifier/name |
| `total_packets` | integer | yes | Total number of packets available in dataset |
| `frequency_hz` | integer | yes | Nominal packet rate (e.g., 40) |
| `num_channels` | integer | yes | Number of neural channels |
| `duration_seconds` | number | yes | Total dataset duration |
| `num_trials` | integer | yes | Number of trials |

### Compatibility aliases
Some consumers currently use different field names. Producers **MAY** provide these aliases, and consumers **SHOULD** accept them when present:

| Alias | Canonical |
|---|---|
| `channel_count` | `num_channels` |
| `sampling_rate_hz` | `frequency_hz` |
| `total_samples` | `total_packets` |
| `trial_count` | `num_trials` |

## `data` payload (`StreamPacket`)
The `data` payload represents one stream tick.

| Field | Type | Required | Semantics |
|---|---:|:---:|---|
| `timestamp` | number | yes | Unix timestamp in seconds (epoch time) |
| `sequence_number` | integer | yes | Monotonic sequence number starting at 0 |
| `spikes` | object | yes | Spike-count features |
| `kinematics` | object | yes | Ground-truth cursor kinematics |
| `intention` | object | yes | Ground-truth target intention |
| `trial_id` | integer 
| null | no | Trial identifier (if available) |
| `trial_time_ms` | number 
| null | no | Time within trial (ms), if available |

### `spikes`
| Field | Type | Required | Semantics |
|---|---:|:---:|---|
| `channel_ids` | array[int] | yes | Stable channel identifiers |
| `spike_counts` | array[int] | yes | Spike counts per channel for this bin |
| `bin_size_ms` | number | yes | Bin width in milliseconds (nominally 25.0) |

`channel_ids.length` **MUST** equal `spike_counts.length`.

### `kinematics`
| Field | Type | Required |
|---|---:|:---:|
| `vx` | number | yes |
| `vy` | number | yes |
| `x` | number 
| null | no |
| `y` | number 
| null | no |

### `intention`
| Field | Type | Required |
|---|---:|:---:|
| `target_id` | integer 
| null | no |
| `target_x` | number 
| null | no |
| `target_y` | number 
| null | no |
| `distance_to_target` | number 
| null | no |

## Timestamp semantics
- `timestamp` is defined as Unix epoch seconds.
- Producers **MUST** use a consistent clock basis per connection.
- Consumers **MUST NOT** compare `timestamp` to monotonic clocks (e.g., browser `performance.now()`).

Recommended network-latency estimate for consumers:
- `latency_ms = Date.now() - (timestamp * 1000)`

(Where `Date.now()` is Unix epoch milliseconds.)
