from fastapi import FastAPI, status, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.Config import configs
from app.utils.uptime import getUptime
from app.db import is_db_connected, init_collection, client
import time
from app.routes.api.v1.admin.admin_router import router as admin_router
from app.routes.api.v1.quiz.quiz_router import router as quiz_router
from app.routes.api.v1.auth.auth import router as auth_router

startTime = time.time()

app = FastAPI(
    title=configs.APP_NAME,
    version=configs.APP_VERSION,
    description=configs.APP_NAME + " API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_db_client():
    if is_db_connected():
        print(f"🚀 @{configs.APP_NAME} v{configs.APP_VERSION} [{configs.PYTHON_ENV}]")
        print("🍀 Database Connected.")
        init_collection()
    else:
        print("❌ Database not Connected - Please check MONGO_DB_URI env.")


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["Health Route"],
    response_class=ORJSONResponse,
)
async def health_route(req: Request):
    """
    Health Route : Returns App details.
    """
    return ORJSONResponse(
        {
            "app": configs.APP_NAME,
            "version": "v" + configs.APP_VERSION,
            "ip": req.client.host,
            "uptime": getUptime(startTime),
            "database": "connected" if is_db_connected() else "disconnected",
            "mode": configs.PYTHON_ENV,
        }
    )


app.include_router(admin_router, tags=["Administrator"], prefix="/api/v1/admin")
app.include_router(quiz_router, tags=["Quiz"], prefix="/api/v1/quiz")
app.include_router(auth_router, tags=["Auth"], prefix="/api/v1/auth")
