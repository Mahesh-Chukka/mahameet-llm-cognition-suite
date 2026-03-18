import time
import uuid
from typing import Callable
from fastapi import Request


def start_timer() -> float:
    return time.perf_counter()


def end_timer(start: float) -> float:
    return (time.perf_counter() - start) * 1000  # ms


def new_request_id() -> str:
    return str(uuid.uuid4())


def log_event(event: str, **kwargs):
    # Simple structured logs (prints JSON-ish)
    payload = {"event": event, **kwargs}
    print(payload)
