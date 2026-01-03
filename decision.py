from policy_store import APPROVED_POLICIES
from contract_store import CONTRACT_OVERRIDES


def decide(user_question: str) -> dict:
    question_lower = user_question.lower()

    for policy in APPROVED_POLICIES:
        if all(keyword in question_lower for keyword in policy["keywords"]):
            for override in CONTRACT_OVERRIDES:
                if override["policy_id"] == policy["id"]:
                    return {
                        "status": "approved",
                        "policy_id": policy["id"],
                        "text": override["override_text"],
                        "source": "contract_override"
                    }

            return {
                "status": "approved",
                "policy_id": policy["id"],
                "text": policy["text"],
                "source": "policy"
            }

    return {
        "status": "refused",
        "reason": "No approved policy fragment matches this question."
    }
