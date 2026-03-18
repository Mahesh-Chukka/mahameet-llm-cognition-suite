from fastapi import FastAPI
from .api.routes_clarity import router as clarity_router
from .core.db import Base, engine
from . import models

app = FastAPI(title="LLM Cognition Backend", version="0.1.0")

Base.metadata.create_all(bind=engine)

app.include_router(clarity_router)


@app.get("/health")
def health():
    return {"status": "ok"}
