from policy_store import APPROVED_POLICIES
from contract_store import CONTRACT_OVERRIDES
from llm_explainer import explain_text

def decide(user_question: str) -> dict:
    question_lower = user_question.lower()

    for policy in APPROVED_POLICIES:
        if all(keyword in question_lower for keyword in policy["keywords"]):
            for override in CONTRACT_OVERRIDES:
                if override["policy_id"] == policy["id"]:
                    explained = explain_text(override["override_text"])
                    return {
                        "status": "approved",
                        "policy_id": policy["id"],
                        "text": explained,
                        "source": "contract_override"
                    }
                
            explained = explain_text(policy["text"])
            return {
                "status": "approved",
                "policy_id": policy["id"],
                "text": explained,
                "source": "policy"
            }

    return {
        "status": "refused",
        "reason": "No approved policy fragment matches this question."
    }
