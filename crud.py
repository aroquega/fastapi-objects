from sqlalchemy.orm import Session
import models
import schemas


def get_object(db: Session, object_id: int):
    return db.query(models.Object).filter(models.Object.id == object_id).first()


def get_objects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Object).offset(skip).limit(limit).all()


def create_object(db: Session, object: schemas.ObjectCreate):
    db_object = models.Object(name=object.name, description=object.description)
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object


def delete_object(db: Session, object_id: int):
    db.query(models.Object).filter(models.Object.id == object_id).delete()
    db.commit()
