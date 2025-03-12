
from fastapi import FastAPI
from models import Base,ToDo
from database import engine
from routers.todo import router as auth_router
from routers.auth import router as todo_rooter
app = FastAPI()

app.include_router (auth_router)
app.include_router(todo_rooter)


Base.metadata.create_all(bind=engine)

