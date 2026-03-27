"""Version 1: minimal claim verification report structure."""


def verify_claim(claim):
    """Print a simple structured verification report for a claim."""
    print("=" * 60)
    print("CLAIM")
    print("-" * 60)
    print(claim)
    print()

    print("SOURCES")
    print("-" * 60)
    print("1. Add source here")
    print("2. Add source here")
    print()

    print("FACTS")
    print("-" * 60)
    print("1. Extract fact from source")
    print("2. Extract fact from source")
    print()

    print("GAPS / CONTRADICTIONS")
    print("-" * 60)
    print("1. Missing data or contradiction")
    print("2. Missing data or contradiction")
    print()

    print("VERDICT")
    print("-" * 60)
    print("UNVERIFIED")
    print("=" * 60)


if __name__ == "__main__":
    sample_claim = (
        "Cerebras delivers significantly lower latency than Nvidia "
        "for large model inference"
    )
    verify_claim(sample_claim)
