# Contributing

## Execution boundary rules

- `interceptor.intercept_and_execute(...)` is the only public execution path.
- `gate.execute(...)` must remain blocked.
- `governance_service.execute(...)` must remain blocked.
- New execution paths must not bypass the interceptor.
- Public boundary failures must return structured `BLOCK`, not exceptions.

## Testing requirements

Tests are required for any governance, token, state, or aperture change.
Run:

```bash
python -m unittest discover -s tests -v
python demo_domain_mismatch.py
python demo_speculative_mode.py
python demo_simulation_speculation.py
python examples/mcp_demo.py
```
