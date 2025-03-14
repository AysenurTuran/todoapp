
from fastapi import FastAPI,Request
from starlette.responses import RedirectResponse
from models import Base,ToDo
from database import engine
from fastapi.staticfiles import StaticFiles
from routers.todo import router as auth_router
from routers.auth import router as todo_rooter
from starlette import status
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root(request:Request):
    return RedirectResponse(url="/todo/todo-page",status_code=status.HTTP_302_FOUND)
app.include_router (auth_router)
app.include_router(todo_rooter)

Base.metadata.create_all(bind=engine)

