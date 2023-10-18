from fastapi import APIRouter

from api.v1.endpoint import frontend, authorization

router = APIRouter()

router.include_router(frontend.router)
router.include_router(authorization.router)
