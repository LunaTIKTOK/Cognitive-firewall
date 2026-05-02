from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gate import KeyRing, PaymentGate, configure_authority, register_tool
from interceptor import intercept_and_execute


class LocalMCPAdapter:
    def __init__(self) -> None:
        self.calls = {"n": 0}

    def tool(self, args: dict) -> dict:
        self.calls["n"] += 1
        return {"ok": True, "args": args}


def _ctx() -> dict:
    return {
        "agent_id": "mcp-demo-agent",
        "tenant_id": "tenant-demo",
        "session_id": "sess-demo",
        "tool_id": "tool.scan",
        "model_id": "model-demo",
        "runtime_id": "runtime-demo",
        "delegated_scope": "tool:scan",
        "nonce": "nonce-demo",
        "jti": "jti-demo",
        "policy_ids": ["policy.constitution.v1"],
        "approval_token": "approved",
        "current_state": "RESEARCH",
        "requested_next_state": "READ_ONLY",
        "allow_secrets": False,
    }


def main() -> int:
    configure_authority(
        key_ring=KeyRing(active_key_id="demo-kid", keys={"demo-kid": "demo-secret"}),
        payment_gate=PaymentGate(wallet_balances={"mcp-demo-agent": 100.0}),
    )
    adapter = LocalMCPAdapter()
    register_tool("tool.scan", adapter.tool)

    allowed = intercept_and_execute(
        {"intent": "query_customer_data", "intent_text": "safe claim", "tool_name": "tool.scan", "tool_args": {"claim": "safe"}, "domain": "finance"},
        _ctx(),
    )
    denied = intercept_and_execute(
        {"intent": "query_customer_data", "intent_text": "gravity model for portfolio", "tool_name": "tool.scan", "tool_args": {"claim": "unsafe"}, "domain": "finance"},
        _ctx(),
    )
    speculative = intercept_and_execute(
        {
            "intent": "invest",
            "intent_text": "forward thesis",
            "tool_name": "tool.scan",
            "tool_args": {"claim": "thesis", "requested_allocation_pct": 1.0},
            "domain": "energy",
            "assumptions": [
                {"assumption": "a", "status": "OBSERVABLE", "confidence": 0.7, "evidence": ["signal"], "falsification_trigger": "x", "critical": True},
                {"assumption": "b", "status": "SPECULATIVE", "confidence": 0.6, "evidence": ["signal"], "falsification_trigger": "y", "critical": False},
            ],
            "confidence_average": 0.65,
        },
        _ctx(),
    )
    def print_summary(name: str, out: dict) -> None:
        print(name)
        print(f"decision: {out.get('decision')}")
        print(f"reason: {out.get('reason')}")
        print(f"executed: {out.get('executed')}")
        if out.get("max_allocation_pct") is not None:
            print(f"max_allocation_pct: {out.get('max_allocation_pct')}")
        if isinstance(out.get("simulation"), dict):
            print(f"survival_rate: {out['simulation'].get('thesis_survival_rate')}")
        if out.get("falsification_triggers"):
            print(f"falsification_triggers: {out.get('falsification_triggers')}")

    print_summary("=== MCP Demo: allowed ===", allowed)
    print_summary("=== MCP Demo: denied ===", denied)
    print_summary("=== MCP Demo: speculative ===", speculative)
    print(f"tool_calls: {adapter.calls['n']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
