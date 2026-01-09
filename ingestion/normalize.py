def normalize_sections(raw_text: str) -> list[dict]:
    sections = []
    current = None

    for line in raw_text.splitlines():
        line = line.strip()
        if line.startswith("SECTION: "):
            if current:
                sections.append(current)
            current = {
                "title": line.replace("SECTION:", "").strip(),
                "lines": []
            }
        elif current and line:
            current["lines"].append(line)
        
    if current:
        sections.append(current)
    return sections

# Extracts structure