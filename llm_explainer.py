## simulated llm

def explain_text(approved_text: str) -> str:
    """
    LLM is used ONLY to reword or calrify already approved text.
    it must not add, remove, or infer new information.
    """

    return(
        "Explanation:\n"
        f"{approved_text}"
    )