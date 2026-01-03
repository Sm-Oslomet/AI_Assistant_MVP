from policy_store import APPROVED_POLICIES


def decide(user_question: str) -> dict:
    question_lower = user_question.lower()

    for policy in APPROVED_POLICIES:
        if all(keyword in question_lower for keyword in policy["keywords"]):
            return {
                "status": "approved",
                "policy_id": policy["id"],
                "text": policy["text"]
            }
        
    return {
        "status": "refused",
        "reason": "No approved content avaliable for this question"
    }