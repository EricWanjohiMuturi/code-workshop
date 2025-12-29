from fastapi import FastAPI

app = FastAPI()

@app.get("/shipment")
def def_shipment():
    return {
        "id":1,
        "content": "Books",
        "status": "In Transit"
    }