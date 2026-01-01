def render_response(decision: dict) -> str:
    if decision["status"] == "refused":
        return(
            "REFUSAL\n"
            "--------\n"
            f"Reason: {decision['reason']}\n"
            "The assistant cannot answer this question."
        )
    
    return "UNEXPECTED STATE"