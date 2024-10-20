import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, delete_table
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("db is clearn")
    await create_table()
    print("db redy to work")
    yield
    print("shut down")


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
