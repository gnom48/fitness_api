from fastapi import FastAPI, APIRouter
from .api import *
from contextlib import asynccontextmanager
from .repository import DBRepository
from .database import create_tables, drop_tables


# & C:\Users\Egorc\Desktop\fitness_api\venv\Scripts\activate.ps1
# uvicorn app.main:app --reload --host localhost --port 8080


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await drop_tables()
    # print("База данных очищена")
    # await create_tables()
    # print("База данных создана")
    print("Запуск сервера ...")
    yield
    print("Выключение сервера ...")


router_main = APIRouter(prefix="/main", tags=["Config"])

@router_main.get("/get_config", status_code=200)
async def get_all_services():
    return await DBRepository.get_config()


app = FastAPI(lifespan=lifespan)
app.include_router(router_main)
app.include_router(router_person)
app.include_router(router_statistics)
app.include_router(router_workout)
