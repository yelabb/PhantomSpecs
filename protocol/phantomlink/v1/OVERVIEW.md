# PhantomLink Streaming Protocol (PLSP) — v1

**Status**: Normative

## Abstract
PhantomLink provides real-time replay/streaming of binned neural spiking features and aligned behavioral ground truth over WebSocket. This document defines the PhantomLink Streaming Protocol (PLSP) v1: transports, message envelope, payload types, and timestamp semantics.

## Scope
This spec standardizes:
- WebSocket endpoints for JSON and binary streaming
- Message envelope and payload schemas
- Semantics for ordering, timestamps, and sequence numbers

This spec does **not** standardize:
- Authentication/authorization
- Dataset formats on disk (NWB/HDF5)
- Neural decoding algorithms (handled by PhantomCore/PhantomLoop)

## Normative language
The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

## Components
- **Producer**: PhantomLink server
- **Consumer**: PhantomLoop (web UI), PhantomCore (native client), other tools

## Message types
PLSP v1 defines two message types:
- `metadata`: stream/session metadata
- `data`: a single stream packet (nominally 40 Hz)

## Compatibility goals
- A consumer that implements PLSP v1 **MUST** be able to decode:
  - JSON stream messages (`/stream/{session_code}`)
  - Binary stream messages (`/stream/binary/{session_code}`) using MessagePack

For backward compatibility with existing consumers, PhantomLink **MAY** include additional fields in payload objects, and consumers **MUST** ignore unknown fields.
