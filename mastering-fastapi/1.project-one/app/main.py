from fastapi import FastAPI #type: ignore
from typing import Any
from app.simple_db import shipments


app = FastAPI()


@app.get("/shipment/latest")
def latest_shipment() -> dict[str, Any]:
    id = max(shipments.keys())
    return shipments[id]



#dynamic path parameters
@app.get("/shipment/{id}")
def get_shipment(id:int) -> dict[str, Any]:
    if id not in shipments:
        return {
            "error details": "Shipment not found"
        }
    return shipments[id]