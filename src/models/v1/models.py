from typing import Optional
from pydantic import BaseModel


class Alarm(BaseModel):
    service: str
    function: str
    error: str
    datetime: str
    comment: Optional[str] = None
