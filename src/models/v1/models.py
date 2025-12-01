from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Layer(str, Enum):
    db = "db"
    python = "python"


class Alert(BaseModel):
    layer: Layer
    service: str
    function: str
    error: str
    datetime: str
    comment: Optional[str] = None
