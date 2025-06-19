import fastapi

router = fastapi.APIRouter(prefix='/private')

@router.get("/meals")
async def fetch_daily_meals():
    return "Total meal count is 20"