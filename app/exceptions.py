from fastapi import Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


# Standard Error Response Model
class ErrorResponse(BaseModel):
    error: str
    message: str
    path: str

#Base class for all the custom exceptions
class CustomException(Exception):
    def __init__(self, name: str, detail: str, status_code: int = status.HTTP_404_NOT_FOUND):
        self.name = name
        self.detail = detail
        self.status_code = status_code

# Specific exceptions
class NotFoundException(CustomException):
    def __init__(self,detail: str = "Resource not found"):
        super().__init__(name="NotFoundError", detail = detail, status_code=status.HTTP_404_NOT_FOUND)

class UnauthorisedException(CustomException):
    def __init__(self, detail: str = "Unauthorised access"):
        super().__init__(name = "UnauthorisedError", detail=detail,status_code=status.HTTP_401_UNAUTHORIZED)

class ValidationException(CustomException):
    def __init__(self, detail: str="Validation failed"):
        super().__init__(name="ValidationFailedError",detail=detail,status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


# Generic exception handler
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.name,
            message=exc.detail,
            path= str(request.url)
        ).model_dump()
    )

#Registry of exceptions to register main.py
exception_handlers = {
    CustomException : custom_exception_handler,
    NotFoundException : custom_exception_handler,
    UnauthorisedException : custom_exception_handler,
    ValidationException : custom_exception_handler,
}

# Common error responses dictionary
global_responses = {
    400: {"model": ErrorResponse, "description": "Bad Request"},
    401: {"model": ErrorResponse, "description": "Unauthorized"},
    404: {"model": ErrorResponse, "description": "Not Found"},
    422: {"model": ErrorResponse, "description": "Validation Error"},
}