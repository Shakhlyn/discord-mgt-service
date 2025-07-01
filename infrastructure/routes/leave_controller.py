import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = fastapi.APIRouter(prefix="/private")

@router.get("/daily-leave")
async def fetch_daily_leave_record():
    return "'a' and 'b' are on leave today"

@router.get("/total-leave")
async def fetch_total_leave_record():
    """
    time range
    user
    :return:
    """
    result = ['a', 'b', 'e', 'z']
    return JSONResponse(content=jsonable_encoder(result))
