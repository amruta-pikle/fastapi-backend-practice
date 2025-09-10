import time

from fastapi import FastAPI, Request

from app.api import sample
from app.day1 import endpoints
from app.Day2 import routes, auth
from app.Day3 import Custom_Exception_Handler
from app.Task_Manager_API import task_manager_auth, tasks_endpoints
from app.exceptions import exception_handlers

app = FastAPI(
    title="My Backend Learning Project",
    description="A project to practice backend development with FastAPI",
    version="1.0.0"
)


# ------------------------- GLOBAL MIDDLEWARE ---------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"{request.method} {request.url} completed in {process_time: .4f}s")
    return response


# include routers

# Sample router
app.include_router(sample.router)

# day1 router
app.include_router(endpoints.router)

# day2 routers
app.include_router(routes.router)
app.include_router(task_manager_auth.router)

# Task Manager API
app.include_router(task_manager_auth.router)

# Add router
app.include_router(Custom_Exception_Handler.router)

# Task Manager routes
app.include_router(task_manager_auth.router)
app.include_router(tasks_endpoints.router)

# Add exception handler (custom exception handling)
app.add_exception_handler(
    Custom_Exception_Handler.CustomException,
    Custom_Exception_Handler.custom_exception_handler
)

for exc_class, handler in exception_handlers.items():
    app.add_exception_handler(exc_class,handler)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend Learning!"}
