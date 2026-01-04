# ingestion/ingest.py

import json
from pathlib import Path
from rules import ALLOWED_SECTIONS, FORBIDDEN_KEYWORDS


INPUT_FILE = Path("ingestion/sample_policy.txt")
OUTPUT_FILE = Path("generated/approved_fragments.json")


def parse_sections(text: str) -> dict:
    sections = {}
    current_section = None

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("SECTION:"):
            current_section = line.replace("SECTION:", "").strip()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)

    return sections


def is_safe(text: str) -> bool:
    lower = text.lower()
    return not any(word in lower for word in FORBIDDEN_KEYWORDS)


def main():
    raw_text = INPUT_FILE.read_text(encoding="utf-8")
    sections = parse_sections(raw_text)

    approved_fragments = []

    for section, lines in sections.items():
        if section not in ALLOWED_SECTIONS:
            continue

        content = " ".join(lines).strip()
        if not content:
            continue

        if not is_safe(content):
            continue

        approved_fragments.append({
            "id": "CLEAN_BUS_INTERIOR_V1",
            "category": "cleaning",
            "location": "CityA",
            "keywords": ["clean", "bus", "interior"],
            "text": content
        })

    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(approved_fragments, indent=2),
        encoding="utf-8"
    )

    print(f"Generated {len(approved_fragments)} approved fragment(s).")


if __name__ == "__main__":
    main()
