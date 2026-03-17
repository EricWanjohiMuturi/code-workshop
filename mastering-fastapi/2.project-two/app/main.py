from fastapi import FastAPI #type:ignore
from typing import Any
from app.simple_db import attributes, categories, products #type: ignore

app = FastAPI()

@app.get("/attributes/")
def all_attributes() -> dict[int, dict[str, Any]]:
    return attributes