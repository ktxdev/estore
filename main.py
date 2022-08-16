from fastapi import FastAPI
from database import Base, engine
from api import api

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api.routes)
