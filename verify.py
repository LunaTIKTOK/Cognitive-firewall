"""Version 1: minimal claim verification report structure."""


def verify_claim(claim, sources, facts, gaps, verdict):
    """Print a simple structured verification report for a claim."""
    print("=" * 60)
    print("CLAIM")
    print("-" * 60)
    print(claim)
    print()

    print("SOURCES")
    print("-" * 60)
    for source in sources:
        print(f"- {source}")
    

    print("FACTS")
    print("-" * 60)
    for fact in facts:
        print(f"- {fact}")

    print("GAPS / CONTRADICTIONS")
    print("-" * 60)
    for gap in gaps:
        print(f"- {gap}")

    print("VERDICT")
    print("-" * 60)
    print("verdict")
    print("=" * 60)


if __name__ == "__main__":
   claims = [
     {
    "claim": "Cerebras delivers significantly lower latency than Nvidia for large model inference "
          
    
    "sources": [
    "Cerebras benchmark or product page describing inference performance",
    "Nvidia documentation or third party benchmark describing GPU inference architecture"
]

"facts": [
    "Cerebras reports lower latency or higher tokens per second for some large model inference workloads",
    "Nvidia large model inference uses multi GPU systems with interconnect overhead"
]

"gaps": [
    "Benchmark conditions may differ across vendors and may not be directly comparable",
    "Vendor reported performance may not generalize across all models and workloads"
]

"verdict": "PARTIALLY VERIFIED"
},


    print("\n" + "=" * 60 + "\n")

{
"claim": "Coinbase and USDC will become the primary settlement layer for AI agents"

   "sources": [
    "Coinbase documentation on Base, USDC, and agent infrastructure",
    "Articles or reports discussing USDC usage and agent based payments"
]

"facts": [
    "USDC is widely used for on chain settlement and stable value transfer",
    "Coinbase provides infrastructure including Base and wallets that can support agent transactions"
]

"gaps": [
    "No guarantee Coinbase will dominate over all competitors in agent settlement",
    "Regulation and competing protocols could change the outcome"
]

"verdict": "UNVERIFIED"

},

{
"claim": "x402 will dominate HTTP-native agent micropayments"

"sources": [
    "Documentation or examples describing x402 or HTTP based agent payments",
    "Articles or posts discussing agent to agent payments over HTTP or API calls"
]

"facts": [
    "x402 is designed to allow payments directly through HTTP requests",
    "Agent systems can call APIs and execute transactions programmatically without human intervention"
]

"gaps": [
    "x402 is still early and not widely adopted across the internet",
    "Other payment protocols or blockchains could compete with HTTP based payment system"
]

"verdict": "UNVERIFIED"

}
]

for c in claims:
    verify_claim(
        c["claim"],
        c["sources"],
        c["facts"],
        c["gaps"],
        c["verdict"]
    )

    print("\n" + "=" * 60 + "\n")
