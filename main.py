from fastapi import FastAPI

app = FastAPI()


@app.get("/objects")
def get_objects():
    pass


@app.post("/objects")
def create_object():
    pass


@app.delete("/objects/{object_id}")
def delete_object(object_id: int):
    pass
