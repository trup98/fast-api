from pydantic import BaseModel
from typing import Optional, Any, List


class ApiResponse(BaseModel):
    status: int
    message: str
    data: Optional[Any] = None


class ErrorDTO(BaseModel):
    timestamp: int
    status: int
    error: Optional[Any] = None
    message: str
    path: str
