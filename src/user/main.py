from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from user.core.config import settings
from user.v1.endpoints.get_user.get_user import router

app = FastAPI(
    description="List of API's for managing users",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    title="User Management",
    version="1.0.0")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix=settings.API_V1_STR)
