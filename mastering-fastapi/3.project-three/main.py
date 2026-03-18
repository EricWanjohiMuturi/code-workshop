from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{id}")
def read_item(id:int):
    return {"My Number": id}

@app.get("/item/{name}")
def read_item(name: str, age: int):
    return {"My Name": name, "My Age": age}