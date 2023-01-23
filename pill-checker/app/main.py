from fastapi import FastAPI
import uvicorn

from api.routes.api import router as api_router
from core.events import create_start_app_handler
from core.config import DEBUG, PROJECT_NAME, VERSION


def get_application() -> FastAPI:

    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router)
    pre_load = False
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()

