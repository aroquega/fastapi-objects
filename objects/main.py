from fastapi import FastAPI, Depends, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from objects import crud, models, schemas
from objects.database import engine, SessionLocal
from objects.template import env

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def get_objects_list_page(db: Session = Depends(get_db)):
    template = env.get_template("objects_list.html")
    objects = crud.get_objects(db)
    return HTMLResponse(content=template.render(objects=objects), status_code=200)


@app.get("/api/objects", response_model=list[schemas.Object])
def get_objects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_objects(db, skip=skip, limit=limit)


@app.post("/api/objects", response_model=schemas.Object, status_code=status.HTTP_201_CREATED)
def create_object(object: schemas.ObjectCreate, db: Session = Depends(get_db)):
    return crud.create_object(db, object=object)


@app.delete("/api/objects/{object_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_object(object_id: int, db: Session = Depends(get_db)):
    crud.delete_object(db, object_id=object_id)
