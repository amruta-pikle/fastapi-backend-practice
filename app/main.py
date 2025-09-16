import time

from fastapi import FastAPI, Request

from app.api import sample
from app.day1 import endpoints
from app.day2 import routes, auth
from app.day3 import Custom_Exception_Handler
from app.Task_Manager_API import task_manager_auth, tasks_endpoints
from app.exceptions import exception_handlers, global_responses
from app.day4.routes import router as notes_router
from app.day5.routes import router as item_router

app = FastAPI(
    title="My Backend Learning Project",
    description="A project to practice backend development with FastAPI",
    version="1.0.0"
)

# Apply global error responses
app = FastAPI(
    title="Daywise FastAPI App",
    responses=global_responses
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

# Add exception handler (custom exception handling)
app.add_exception_handler(
    Custom_Exception_Handler.CustomException,
    Custom_Exception_Handler.custom_exception_handler
)

for exc_class, handler in exception_handlers.items():
    app.add_exception_handler(exc_class,handler)


# include routers

# Sample router
app.include_router(sample.router)

# day1 router
app.include_router(endpoints.router)

# day2 routers
app.include_router(routes.router)
app.include_router(task_manager_auth.router)

#day4 router
app.include_router(notes_router)

#day5 router
app.include_router(item_router)



# Task Manager API
app.include_router(task_manager_auth.router)

# Add router
app.include_router(Custom_Exception_Handler.router)

# Task Manager routes
app.include_router(task_manager_auth.router)
app.include_router(tasks_endpoints.router)









@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Backend Learning!"}
