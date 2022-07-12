from fastapi import APIRouter

from gema.api.convert import router as convert

router = APIRouter()
router.include_router(convert, prefix="/convert", tags=["Convert"])
