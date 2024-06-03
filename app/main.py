from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from typing import Tuple, Dict, Optional
from app.routers.v1.auth import auth
from app.routers.v1.test import test
from app.routers.v1.admin import admin

from app.core.config.env_variables import get_env_vars

app_config: Dict[str, Optional[str]] = {"title": "Role Based JWT Auth", "version": "1.0.0", "docs_url": "/", 
                                        "description": "Implementation of custom JWT role based authentication"}

env = get_env_vars()

SHOW_DOCS_ENV: Tuple[str] = ("LOCAL", "STAGING")

if env.ENVIRONMENT not in SHOW_DOCS_ENV:
    app_config["openapi_url"] = None

app = FastAPI(**app_config)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080/"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"]
)

app.include_router(auth, prefix="/api/v1")
app.include_router(test, prefix="/api/v1")
app.include_router(admin, prefix="/api/v1")


def custom_openapi_jwt():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app_config["title"],
        version=app_config["version"],
        description=app_config["description"],
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema
        
app.openapi = custom_openapi_jwt
