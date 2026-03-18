from sqlalchemy import Boolean, Column, Integer, String, Text
from .core.db import Base

class ClarityAnalysis(Base):
    __tablename__ = "clarity_analyses"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    framing = Column(Text, nullable=False)
    emotional_intensity = Column(Integer, nullable=False)
    confidence = Column(String(20), nullable=False)
    validation_passed = Column(Boolean, nullable=False)
    model = Column(String(100), nullable=False)