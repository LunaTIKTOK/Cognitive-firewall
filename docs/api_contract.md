# API Contract

## Public entrypoint

`interceptor.intercept_and_execute(intent, actor_context)`

## Blocked direct paths

- `gate.execute(...)` is intentionally blocked.
- `governance_service.execute(...)` is intentionally blocked.

## Intent schema (minimum)

- `intent`: str
- `intent_text`: str
- `tool_name`: str
- `tool_args`: dict
- `domain`: str

Optional speculative fields:

- `assumptions`: list[dict]
- `confidence_average`: float
- `requested_allocation_pct`: float
- `run_simulation`: bool
- `simulation_count`: int
- `simulation_seed`: int

## Actor context schema (minimum)

- `agent_id`: str
- `tenant_id`: str
- `session_id`: str
- `tool_id`: str
- `policy_ids`: list[str]
- `approval_token`: str
- `current_state`: str
- `requested_next_state`: str
- `allow_secrets`: bool
- `solvency_ok`: bool
- `reputation_tier`: str

## Output schema

Always returns envelope:

- `decision`: `ALLOW` | `SPECULATE` | `BLOCK`
- `executed`: bool
- `reason`: str | None
- `violations`: list | None
- `epistemic_status`: str | None
- `speculative`: bool
- `max_allocation_pct`: float | None
- `confidence_average`: float | None
- `falsification_triggers`: list
- `simulation`: dict | None

Optional simulation fields (inside `simulation`):

- `simulation_count`
- `thesis_survival_rate`
- `sensitivity`
- `fragile_assumptions`
- `max_allocation_pct`
- `falsification_triggers`

## Token boundary notes

Token issuance occurs only after domain/uncertainty/simulation/runtime-governance checks pass. Direct tool execution without governed token path is not allowed.
