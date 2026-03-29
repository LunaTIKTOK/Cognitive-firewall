# Claim-Verify

Claim-Verify is a pre-execution risk engine for humans and AI agents.

It evaluates claims, tasks, or proposed actions before execution by estimating:

- structural validity
- evidentiary support
- decision risk
- expected cost of error
- token / compute waste risk

It then assigns an execution permission:

- allow
- allow_with_warning
- block

## Purpose

Claim-Verify exists to:

- reduce decision error
- prevent execution on unsupported or invalid claims
- minimize wasted compute
- enforce a consistent pre-action evaluation layer

It does not attempt to determine absolute truth.  
It evaluates whether acting on a claim is justified given available evidence and structure.

## Core Behavior

For any input, the system:

1. Normalizes the claim (including multilingual input)
2. Checks structural validity (e.g. absolute or impossible claims)
3. Estimates evidence strength and ambiguity
4. Calculates decision and economic risk
5. Determines whether execution should proceed

## Usage

Run with structured input:

```bash
python verify.py --input claims.json
```
