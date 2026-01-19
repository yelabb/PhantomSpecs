# Changelog

All notable changes to PhantomSpecs will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- PhantomLoop decoder interface JSON schema (`schemas/phantomloop/v1/decoder.schema.json`)

### Changed
- Updated validation script to cover all component schemas

## [1.0.0] - 2026-01-18

### Added
- **PhantomLink PLSP v1**
  - Streaming envelope + data/metadata models
  - WebSocket transport specification (`TRANSPORT_WS.md`)
  - Message types and payload schemas (`TYPES.md`)
  - JSON schemas for message, metadata, and packet validation
  - Test vectors for round-trip validation

- **PhantomLoop v1**
  - Client contract for PLSP consumption (`OVERVIEW.md`)
  - Decoder interface specification (`DECODER_INTERFACE.md`)
  - Latency computation and buffering requirements

- **PhantomCore v1**
  - Stream compatibility requirements (`STREAM_COMPATIBILITY.md`)
  - MessagePack decoding expectations

- **PhantomCodec v1**
  - 8-byte frame header specification (`FRAME_HEADER.md`)
  - Strategy registry with 4 strategies (`STRATEGIES.md`)
  - JSON schema for header model validation
  - Binary test vectors with hex examples

- **Tooling**
  - `validate_vectors.py` for schema + vector validation
  - Versioning policy (`VERSIONING.md`)
