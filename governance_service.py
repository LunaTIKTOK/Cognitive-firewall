from __future__ import annotations

from typing import Any

from gate import execute as _execute
from gate import issue_governance_token as _issue_governance_token
from intent_classification import classify_intent
from runtime_governance import RuntimeState, evaluate_runtime_governance


DEFAULT_POLICY_PACKS = [
    "packs/financial_pack.json",
    "packs/privacy_pack.json",
    "packs/brand_pack.json",
    "packs/system_pack.json",
]


def evaluate_request(
    *,
    intent: str,
    tool_name: str,
    actor_context: dict[str, Any],
    tool_args: dict[str, Any],
    current_state: RuntimeState,
    requested_next_state: RuntimeState,
):
    intent_class = classify_intent(tool_name, intent)
    return evaluate_runtime_governance(
        current_state=current_state,
        requested_next_state=requested_next_state,
        tool_name=tool_name,
        intent_class=intent_class,
        actor_identity_ok=bool(actor_context.get("agent_id")),
        approval_token_present=bool(actor_context.get("approval_token")),
        solvency_ok=bool(actor_context.get("solvency_ok", True)),
        reputation_tier=str(actor_context.get("reputation_tier", "TRUSTED")),
        soft_override_justification=actor_context.get("override_justification"),
        context=tool_args,
        policy_pack_paths=DEFAULT_POLICY_PACKS,
    )


def issue_governance_token(intent: str, actor_context: dict, tool_name: str, tool_args: dict) -> str:
    current_state = RuntimeState[str(actor_context.get("current_state", RuntimeState.RESEARCH.value))]
    requested_next_state = RuntimeState[str(actor_context.get("requested_next_state", RuntimeState.READ_ONLY.value))]
    decision = evaluate_request(
        intent=intent,
        tool_name=tool_name,
        actor_context=actor_context,
        tool_args=tool_args,
        current_state=current_state,
        requested_next_state=requested_next_state,
    )
    if decision.status == "DENY":
        reason = decision.correction_requirement.required_action if decision.correction_requirement else "GOVERNANCE_DENY"
        raise RuntimeError(f"UNAUTHORIZED_EXECUTION: governance denied token issuance ({reason})")
    return _issue_governance_token(intent, actor_context, tool_name, tool_args)


def execute(intent: str, actor_context: dict, tool_name: str, tool_args: dict):
    return _execute(intent, actor_context, tool_name, tool_args)
