from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base
from app.api.users import router as users_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users_router)

