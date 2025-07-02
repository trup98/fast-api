from fastapi import FastAPI
from api import user_route
from db.base_class import Base
from db.database import engine
from modals import user_modal

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User CRUD API",
    version="1.0.0"
)

app.include_router(user_route.router)
