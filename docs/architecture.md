# Cognitive Firewall Aperture Runtime Architecture

```mermaid
flowchart LR
  A[Agent intent] --> B[Interceptor]
  B --> C[Domain Mismatch Gate]
  C --> D[Uncertainty Gate]
  D --> E[Simulation Gate]
  E --> F[Runtime Governance]
  F --> G[Token Issuance]
  G --> H[Internal Authorized Execution]
  H --> I[MCP Executor]
  I --> J[Audit Receipt]
```

This architecture is an agent execution aperture: it controls consequential tool execution between reasoning and action, and is not generic network security middleware.
