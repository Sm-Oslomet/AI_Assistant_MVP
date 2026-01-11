from fragment_store import load_fragments
from semantic_retrieval import SemanticRetriever
from policy_store import APPROVED_POLICIES
from contract_store import CONTRACT_OVERRIDES
from llm_explainer import explain_text

_fragments = load_fragments()
_retriever = SemanticRetriever(_fragments)


def decide(user_question: str) -> dict:
    matches = _retriever.retrieve(user_question)

    if not matches:
        return{
            "status": "refused",
            "reason": "No sufficiently relevant approved fragment found."
        }
    
    top = matches[0]

    # contract override check

    for override in CONTRACT_OVERRIDES:
        if override["policy_id"] == top["id"]:
            return {
                "status": "approved",
                "policy_id": top["id"],
                "text": explain_text(override["override_text"]),
                "source": "contract_override"
            }
        
    return {
        "status": "approved",
        "policy_id": top["id"],
        "text": explain_text(top["text"]),
        "source": "policy_fragment"
    }