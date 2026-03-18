import json
from ..core.llm import llm
from ..core.config import settings
from ..core.schemas import ClarityLensReport
from ..core.guards import guard

SYSTEM = (
    "You are Clarity Lens, a careful text analyst. "
    "Be neutral. Do not moralize. "
    "If uncertain, say so and lower confidence."
)

async def analyze_influence(text: str):
    prompt = f"""
Analyze the following text for framing and persuasion.

Return:
- summary (2-4 sentences, neutral)
- framing (how it shapes interpretation)
- emotional_intensity (0-100)
- confidence (low/medium/high)

TEXT:
{text}
""".strip()

    report: ClarityLensReport = llm.chat.completions.create(
        model=settings.OPENAI_MODEL,
        response_model=ClarityLensReport,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    )

    validated = guard.validate(json.dumps(report.model_dump()))
    validation_passed = bool(getattr(validated, "validated_output", None))

    if validation_passed:
        final_report = ClarityLensReport(**validated.validated_output)
    else:
        report.confidence = "low"
        final_report = report

    return final_report, validation_passed