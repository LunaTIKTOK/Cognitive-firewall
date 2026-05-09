# Ticket Issuance Flow

## Flow

1. `evaluate_request(...)` runs runtime governance evaluation.
2. If decision is not `DENY`, a one-time `governance_issuance_ticket` is minted.
3. `issue_governance_token(...)` consumes the ticket.
4. Ticket fingerprint is validated against intent/tool/payload/context.
5. Runtime governance is evaluated again at issuance boundary.
6. Governance token is signed and returned for authorized execution.

## Issuance ticket vs governance token

- **Issuance ticket**: short-lived, one-time pre-token authorization marker.
- **Governance token**: signed execution authority bound to payload hash and context.

## Why one-time tickets

One-time consumption prevents replaying ticket material to mint extra execution authority.

## Why payload-bound tokens

Payload binding prevents a valid token from being reused with modified tool arguments.

## Why execution still requires interceptor

The interceptor is the only public execution boundary; direct `gate.execute(...)` and `governance_service.execute(...)` stay blocked to prevent bypass paths.
