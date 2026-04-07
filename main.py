from fastapi import FastAPI
from routers import router
from database import engine, Base
from models import TaskDB

Base.metadata.create_all(bind=engine)


app = FastAPI()



app.include_router(router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "healthy"}