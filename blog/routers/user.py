from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user




router = APIRouter(
    prefix='/user',
    tags=['Users']
)

get_db = database.get_db



@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
     
     return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
     return user.show_user(id, db)

@router.get('/', response_model=list[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
   return user.all(db)