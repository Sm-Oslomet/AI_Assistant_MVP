def render_response(decision: dict) -> str:
    if decision["status"] == "approved":
        return(
            "APPROVED ANSWER\n"
            "----------------\n"
            f"{decision['text']}"
        )
    
    if decision["status"] == "refused":
        return(
            "REFUSAL\n"
            "--------\n"
            f"Reason: {decision['reason']}\n"
            "The assistant cannot answer this question."
        )
    
    return "UNEXPECTED STATE"