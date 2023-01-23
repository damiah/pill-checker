from fastapi import APIRouter
import uvicorn
from api.routes import test, predictor, pills

router = APIRouter()
router.include_router(test.router)
router.include_router(predictor.router, tags=["predictor"])
router.include_router(pills.router)

@router.get("/")
async def root():
    return {"message": "Hello World"}

 # at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)