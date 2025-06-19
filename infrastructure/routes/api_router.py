from fastapi import APIRouter

from infrastructure.routes import meal_controller, leave_controller, attendance_controller

router = APIRouter(prefix="/discord-mgt/api/v1")

router.include_router(meal_controller.router)
router.include_router(leave_controller.router)
router.include_router(attendance_controller.router)