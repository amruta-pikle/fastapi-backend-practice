from fastapi import FastAPI
from app.api import sample

app = FastAPI(
    title="My Backend Learning Project",
    description="A project to practice backend development with FastAPI",
    version="1.0.0"
)

# include routers
app.include_router(sample.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend Learning!"}