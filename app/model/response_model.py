from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    message: str = None
    data: T = None
