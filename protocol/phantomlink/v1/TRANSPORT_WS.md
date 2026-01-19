# PLSP v1 — WebSocket Transport

## Endpoints
PhantomLink exposes two WebSocket endpoints for the same logical stream:

- **JSON**: `GET /stream/{session_code}`
- **Binary (MessagePack)**: `GET /stream/binary/{session_code}`

Both endpoints accept optional query parameters:
- `trial_id` (integer, optional)
- `target_id` (integer, optional)

## Session code
`session_code` identifies an isolated playback session.
- PhantomLink **MUST** treat different session codes as independent playback state.

## WebSocket handshake
- The server **MUST** accept standard WebSocket connections.
- Consumers **SHOULD** set `binaryType = "arraybuffer"` (or equivalent) when using the binary endpoint.
- No WebSocket subprotocol is required for v1.

## Message ordering
- The server **MUST** send exactly one `metadata` message first after connection acceptance.
- The server **MUST** then send a sequence of `data` messages.
- Messages **MUST** be ordered by `sequence_number` (monotonic increasing by 1) within a connection.

## Delivery and loss
WebSockets run over TCP; however:
- Consumers **MUST** tolerate temporary pauses, reconnects, and duplicate delivery across reconnection boundaries.
- Consumers **SHOULD** treat `sequence_number` as the de-duplication key.

## Client → server control
PLSP v1 does not standardize WebSocket control messages.

Playback control in the current system is provided by HTTP endpoints:
- `POST /api/control/{session_code}/pause`
- `POST /api/control/{session_code}/resume`
- `POST /api/control/{session_code}/seek?position_seconds=...`

A future PLSP revision may define WebSocket control frames; v1 consumers **MUST NOT** assume their existence.

## Error handling
- On unrecoverable server errors, PhantomLink **MAY** close the socket with code `1011`.
- Consumers **SHOULD** surface the close reason if provided.
