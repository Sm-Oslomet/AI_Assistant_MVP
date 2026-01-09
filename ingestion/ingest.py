# ingestion/ingest.py

import json
from pathlib import Path
from rules import ALLOWED_SECTIONS, FORBIDDEN_KEYWORDS
from normalize import normalize_sections
from fragment import fragment_section

INPUT_FILE = Path("ingestion/sample_policy.txt")
OUTPUT_FILE = Path("generated/approved_fragments.json")


def is_safe(text: str) -> bool:
    lower = text.lower()
    return not any(word in lower for word in FORBIDDEN_KEYWORDS)


def main():
    raw_text = INPUT_FILE.read_text(encoding="utf-8")
    sections = normalize_sections(raw_text)

    approved_fragments = []

    for section in sections:
        if section["title"] not in ALLOWED_SECTIONS:
            continue

        fragments = fragment_section(section)

        for i, fragment in enumerate(fragments):
            if not is_safe(fragment):
                continue

            approved_fragments.append({
                "id": f"CLEAN_BUS_INTERIOR_{i+1}",
                "category": "cleaning",
                "location": "CityA",
                "keywords": ["clean", "bus", "interior"],
                "text": fragment
            })


    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(approved_fragments, indent=2),
        encoding="utf-8"
    )

    print(f"Generated {len(approved_fragments)} approved fragment(s).")


if __name__ == "__main__":
    main()
