from fastapi import FastAPI, HTTPException
from api import user_route
from db.base_class import Base
from db.database import engine
from modals import user_modal
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from schemas.response_schema import ErrorDTO
import time

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User CRUD API",
    version="1.0.0"
)

app.include_router(user_route.router)


# Handles RequestValidationError (e.g., Pydantic schema validation)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Customize each error message
    custom_errors = []
    for err in exc.errors():
        loc = err.get("loc", [])
        field = loc[-1] if loc else "field"
        msg = err.get("msg", "Invalid value")
        custom_errors.append(f"{field}: {msg.capitalize()}")

    return JSONResponse(
        status_code=422,
        content=ErrorDTO(
            timestamp=int(time.time() * 1000),
            status=422,
            error=custom_errors,
            message="Validation failed",
            path=str(request.url)
        ).dict()
    )


# Handles manually raised HTTPException (e.g., user not found, duplicate email)
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorDTO(
            timestamp=int(time.time() * 1000),
            status=exc.status_code,
            error=None,
            message=exc.detail,
            path=str(request.url)
        ).dict()
    )
