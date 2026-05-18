import json
from pathlib import Path

from app.config import RAW_DATA_DIR


def save_raw_json(filename: str, data: dict) -> Path:
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    path = RAW_DATA_DIR / filename

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    return path
