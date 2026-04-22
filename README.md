# Constraint-Engine

Constraint-Engine is **runtime governance infrastructure for agents**.

This repository has shifted from **validator** to **governor**:

- validator: classify/risk score outputs
- governor: define and enforce pre-action execution boundaries

## Governance pipeline

The runtime model is:

1. **permissioning** (state + policy + identity + solvency)
2. **execution** (governed token-bound call path)
3. **correction** (deterministic corrective routing)
4. **audit** (violation and economic traceability)

## Runtime state governance

Supported operation modes:

- `RESEARCH`
- `DRAFTING`
- `READ_ONLY`
- `TRANSACTION`
- `PRIVILEGED`
- `HUMAN_REVIEW`
- `QUARANTINED`

Policies can target states and transitions and can deny or permit state movement.

## Constraint hierarchy

Constraint levels:

- `HARD` (immutable)
- `SOFT` (override requires explicit justification)
- `GOAL` (task/session scoped)

Constraint packs (examples):

- `packs/financial_pack.json`
- `packs/privacy_pack.json`
- `packs/brand_pack.json`
- `packs/system_pack.json`

## Intent classes

Intent classes are separated from raw tool names:

- `DATA_ACCESS`
- `DATA_EXPORT`
- `COMMUNICATION`
- `PAYMENT`
- `TRADE`
- `SYSTEM_MODIFICATION`
- `AUTHORIZATION`
- `UNKNOWN`

## Sidecar-friendly API

`governance_service.py` exposes:

- `evaluate_request(...)`
- `issue_governance_token(...)`
- `execute(...)`

Designed for future FastAPI/gRPC sidecar deployment.

## Boundary API

Public boundary functions in `gate.py`:

```python
configure_authority(...)
register_tool(...)
issue_governance_token(intent, actor_context, tool_name, tool_args)
execute(intent, actor_context, tool_name, tool_args)
```

## Demo

```bash
python middleware_example.py
```
