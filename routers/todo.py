from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import FastAPI,APIRouter, Depends, Path, HTTPException
from starlette import status
from models import Base,ToDo
from database import engine, SessionLocal
from typing import Annotated
from routers.auth import get_current_user

router=APIRouter(prefix="/todo",tags=["Todo"])


class TodoRequest(BaseModel):
      title:str=Field(...,min_length=3,max_length=50)
      description:str=Field(...,min_length=3,max_length=200)
      priority:int=Field(...,gt=0,lt=6)
      completed:bool=False


def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]
user_dependency = Annotated[dict , Depends(get_current_user)]

@router.get("/")
async def read_all(user: user_dependency,db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return db.query(ToDo).filter(ToDo.owner_id==user.get("id")).all()

@router.get("/read_by_id/{todo_id}",status_code=status.HTTP_200_OK  )
async def read_by_id(user:user_dependency,db:db_dependency,todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    todo=db.query(ToDo).filter(ToDo.id==todo_id).filter(ToDo.owner_id==user.get("id")).first()
    if ToDo is not None:
        return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_todo(user:user_dependency ,db:db_dependency,todo_request:TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    todo=ToDo(**todo_request.model_dump(),owner_id=user.get("id"))
    db.add(todo)
    db.commit()

@router.put("/update/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(user:user_dependency,db:db_dependency,todo_request:TodoRequest,todo_id:int =Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    todo=db.query(ToDo).filter(ToDo.id==todo_id).filter(ToDo.owner_id==user.get("id")).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    todo.title=todo_request.title
    todo.description=todo_request.description
    todo.priority=todo_request.priority
    todo.completed=todo_request.completed
    db.add(todo)
    db.commit()

@router.delete("/delete/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user:user_dependency,db:db_dependency, todo_id:int=Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    todo=db.query(ToDo).filter(ToDo.id==todo_id).filter(ToDo.owner_id==user.get("id")).first()
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.query(ToDo).filter(ToDo.id==todo_id).first()
    db.commit()