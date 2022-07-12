from fastapi import APIRouter

from gema.api.convert import router as convert
from gema.api.info import router as info

router = APIRouter()
router.include_router(convert, prefix="/convert", tags=["Convert"])
router.include_router(info, prefix="/info", tags=["Info"])
