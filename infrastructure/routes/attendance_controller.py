from fastapi import APIRouter
from pydantic import BaseModel

from app.core.constant.http_status_code import HttpStatusCode

router = APIRouter(prefix="/private", tags=["Attendance"])


class AttendanceBody(BaseModel):
    user: str


@router.get("/attendance",)
async def fetch_attendance():
    """Retrieve the total number of attendance records"""
    return {"total_attendance": 50}


@router.post("/attendance")
async def submit_attendance(body: AttendanceBody):
    """Submit a new attendance record for a user
    """
    result = {
        "description": "Attendance record saved successfully",
        "status": HttpStatusCode.CREATED.name,
        "user": body.user,
    }

    return result
