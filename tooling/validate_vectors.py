import base64
import json
from pathlib import Path

import jsonschema
import msgpack

ROOT = Path(__file__).resolve().parents[1]


def _load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _load_schema(path: Path):
    schema = _load_json(path)
    jsonschema.Draft202012Validator.check_schema(schema)
    return schema


def validate_phantomlink_v1() -> None:
    schema_dir = ROOT / "schemas" / "phantomlink" / "v1"
    message_schema = _load_schema(schema_dir / "message.schema.json")

    vectors_dir = ROOT / "vectors" / "phantomlink" / "v1"
    for name in ["metadata.json", "packet.json"]:
        obj = _load_json(vectors_dir / name)
        jsonschema.validate(instance=obj, schema=message_schema)

    # Optional: generate MessagePack bytes and ensure round-trip decode
    for name in ["metadata.json", "packet.json"]:
        obj = _load_json(vectors_dir / name)
        packed = msgpack.packb(obj, use_bin_type=True)
        unpacked = msgpack.unpackb(packed, raw=False)
        if unpacked != obj:
            raise AssertionError(f"MessagePack round-trip mismatch for {name}")


def validate_phantomcodec_v1() -> None:
    schema_path = ROOT / "schemas" / "phantomcodec" / "v1" / "header_model.schema.json"
    schema = _load_schema(schema_path)

    examples_path = ROOT / "vectors" / "phantomcodec" / "v1" / "header_examples.json"
    examples = _load_json(examples_path)

    for ex in examples.get("examples", []):
        model = ex["model"]
        jsonschema.validate(instance=model, schema=schema)

        # Validate hex bytes match the model (PHDC + version + channel_count + selector)
        hex_str = ex["bytes_hex"]
        raw = bytes.fromhex(hex_str)
        if len(raw) != 8:
            raise AssertionError(f"{ex['name']}: expected 8 bytes, got {len(raw)}")
        if raw[0:4] != b"PHDC":
            raise AssertionError(f"{ex['name']}: bad magic")
        if raw[4] != 0x01:
            raise AssertionError(f"{ex['name']}: bad version")
        channel_count = (raw[5] << 8) | raw[6]
        if channel_count != model["channel_count"]:
            raise AssertionError(f"{ex['name']}: channel_count mismatch")
        selector = raw[7]
        strategy_id = selector >> 2
        rice_k = selector & 0x03
        if strategy_id != model["strategy_id"] or rice_k != model["rice_k"]:
            raise AssertionError(f"{ex['name']}: selector mismatch")


def main() -> None:
    validate_phantomlink_v1()
    validate_phantomcodec_v1()
    print("OK: schemas and vectors validate")


if __name__ == "__main__":
    main()
