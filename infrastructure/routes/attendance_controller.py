# import fastapi
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
#
# router = fastapi.APIRouter(prefix="/private")
#
# class AttendanceBody(BaseModel):
#     user: str | None = None
#
# @router.get("/attendance")
# async def fetch_attendance():
#     return 'Total attendance is 50'
#
# @router.post("/attendance")
# async def submit_attendance(body: AttendanceBody):
#     print(body)
#     des = "Attendance record is saved successfully"
#     result = {
#         "description": des,
#     }
#
#     if body.user is not None:
#         result.update({'user': body.user})
#
#     return JSONResponse(content=jsonable_encoder(result))


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
