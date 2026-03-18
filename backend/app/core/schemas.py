from pydantic import BaseModel, Field
from typing import Literal

Confidence = Literal["low", "medium", "high"]


class ClarityLensReport(BaseModel):
    summary: str = Field(..., description="Neutral summary in 2-4 sentences.")
    framing: str = Field(..., description="What framing is used and how it shapes interpretation.")
    emotional_intensity: int = Field(..., ge=0, le=100, description="0-100 intensity score.")
    confidence: Confidence = Field(..., description="How confident the system is.")


class ClarityMeta(BaseModel):
    validation_passed: bool
    model: str
    input_chars: int
    latency_ms: float


class ClarityResponse(BaseModel):
    report: ClarityLensReport
    meta: ClarityMeta


class ClarityHistoryItem(BaseModel):
    id: int
    input_text: str
    summary: str
    framing: str
    emotional_intensity: int
    confidence: Confidence
    validation_passed: bool
    model: str

    class Config:
        from_attributes = True
