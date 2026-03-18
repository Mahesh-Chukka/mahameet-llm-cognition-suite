import time
from typing import List
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from ..api.deps import get_db
from ..core.config import settings
from ..core.schemas import ClarityHistoryItem, ClarityMeta, ClarityResponse
from ..models import ClarityAnalysis
from ..services.clarity_service import analyze_influence

router = APIRouter(prefix="/clarity", tags=["clarity"])


class ClarityRequest(BaseModel):
    text: str = Field(..., min_length=20, max_length=15000)


@router.post("/analyze", response_model=ClarityResponse)
async def analyze(req: ClarityRequest, request: Request, db: Session = Depends(get_db)):
    start = time.perf_counter()

    report, validation_passed = await analyze_influence(req.text)

    latency_ms = round((time.perf_counter() - start) * 1000, 2)

    analysis_row = ClarityAnalysis(
        input_text=req.text,
        summary=report.summary,
        framing=report.framing,
        emotional_intensity=report.emotional_intensity,
        confidence=report.confidence,
        validation_passed=validation_passed,
        model=settings.OPENAI_MODEL,
    )

    db.add(analysis_row)
    db.commit()
    db.refresh(analysis_row)

    return ClarityResponse(
        report=report,
        meta=ClarityMeta(
            validation_passed=validation_passed,
            model=settings.OPENAI_MODEL,
            input_chars=len(req.text),
            latency_ms=latency_ms,
        ),
    )


@router.get("/history", response_model=List[ClarityHistoryItem])
def get_history(db: Session = Depends(get_db)):
    rows = (
        db.query(ClarityAnalysis)
        .order_by(ClarityAnalysis.id.desc())
        .limit(20)
        .all()
    )
    return rows