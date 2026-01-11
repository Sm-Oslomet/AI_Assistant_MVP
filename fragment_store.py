import json
from pathlib import Path

FRAGMENTS_FILE = Path("generated/approved_fragments.json")

def load_fragments():
    return json.loads(FRAGMENTS_FILE.read_text(encoding="utf-8"))
