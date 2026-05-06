# Demo Output Samples

## `python demo_domain_mismatch.py`

```text
=== Domain Mismatch Demo Summary ===
decision: BLOCK
reason: DOMAIN_MISMATCH
executed: False
```

## `python demo_speculative_mode.py`

```text
=== Speculative Mode Demo Summary ===
decision: SPECULATE
reason: None
executed: True
max_allocation_pct: 2.0
falsification_triggers: ['AI load growth decelerates below grid expansion', 'PPA term lengths contract materially', 'SMR deployment accelerates ahead of baseline']
```

## `python demo_simulation_speculation.py`

```text
=== Simulation Speculation Demo Summary ===
decision: SPECULATE
reason: None
executed: True
max_allocation_pct: 1.0
survival_rate: 0.741
falsification_triggers: ['AI compute demand growth drops below base trend', 'grid expansion delay drops below base trend', 'hyperscaler long-term power contracting drops below base trend']
```

## `python examples/mcp_demo.py`

```text
=== MCP Demo: allowed ===
decision: ALLOW
reason: None
executed: True
=== MCP Demo: denied ===
decision: BLOCK
reason: DOMAIN_MISMATCH
executed: False
=== MCP Demo: speculative ===
decision: SPECULATE
reason: None
executed: True
max_allocation_pct: 2.0
falsification_triggers: ['x', 'y']
tool_calls: 2
```
