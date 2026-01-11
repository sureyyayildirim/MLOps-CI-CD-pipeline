import json
from pathlib import Path

def load_metadata(path: str = "data/metadata.json") -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
