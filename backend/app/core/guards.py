from guardrails import Guard
from guardrails.hub import ValidLength
from .schemas import ClarityLensReport

guard = Guard.for_pydantic(ClarityLensReport)

# Use JSONPath to point to the exact field inside the output object
guard.use(ValidLength(min=20, max=600), on="$.summary")
guard.use(ValidLength(min=20, max=900), on="$.framing")