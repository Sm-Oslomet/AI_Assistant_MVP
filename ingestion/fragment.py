def fragment_section(section: dict) -> list[str]:
    """
    Split a section into atomic fragments.
    Each sentence becomes one fragment.
    """

    fragments = []

    for line in section["lines"]:
        sentences = [s.strip() for s in line.split(".") if s.strip()]
        fragments.extend(sentences)

    return fragments

# Produces atomic statements