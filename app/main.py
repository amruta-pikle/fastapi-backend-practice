from fastapi import FastAPI
from app.api import sample
from app.day1 import endpoints

app = FastAPI(
    title="My Backend Learning Project",
    description="A project to practice backend development with FastAPI",
    version="1.0.0"
)

# include routers

#Include Sample router
app.include_router(sample.router)

# Include day1 router
app.include_router(endpoints.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend Learning!"}