import asyncio
from app.services.clarity_service import analyze_influence

CASES = [
    ("emotional_short", "They are ruining everything. Wake up and fight back."),
    (
        "balanced_policy",
        "Supporters say the policy reduces costs; critics say it shifts burdens and may create unintended effects.",
    ),
    (
        "fear_framing",
        "The country is collapsing and only drastic action can save it right now.",
    ),
]


async def main():
    for name, text in CASES:
        report, validation_passed = await analyze_influence(text)
        print("\n===", name, "===")
        print("validation_passed:", validation_passed)
        print("confidence:", report.confidence)
        print("emotional_intensity:", report.emotional_intensity)
        print("summary:", report.summary)
        print("framing:", report.framing)


if __name__ == "__main__":
    asyncio.run(main())
