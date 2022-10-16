from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from user_management.core.config import settings
from user_management.v1.endpoints.create_user.create_user import router as CreateUserRouter
from user_management.v1.endpoints.delete_user.delete_user import router as DeleteUserRouter
from user_management.v1.endpoints.get_user.get_user import router as GetUserRouter

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

app.include_router(CreateUserRouter, prefix=settings.API_V1_STR)
app.include_router(DeleteUserRouter, prefix=settings.API_V1_STR)
app.include_router(GetUserRouter, prefix=settings.API_V1_STR)
