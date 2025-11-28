from lib.config import settings
from fastapi.responses import JSONResponse


NOT_SIGNED = JSONResponse(
    status_code=200,
    content={
        "result": "invalid_data"
    }
)


SYSTEM_ERROR = JSONResponse(
    status_code=500,
    content={
        "result": "system_error",
        "error_message": settings.SYSTEM_ERROR
    }
)


DB_ERROR = JSONResponse(
    status_code=500,
    content={
        "result": "db_error",
        "error_message": settings.DB_ERROR
    }
)
