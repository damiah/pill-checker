from fastapi import APIRouter
import uvicorn
from api.routes import pills, upload

router = APIRouter()
router.include_router(pills.router)
router.include_router(upload.router)

@router.get("/")
async def root():
    return {"message": "Hello World"}
