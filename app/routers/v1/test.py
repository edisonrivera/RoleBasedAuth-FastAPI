from app.model.response_model import ResponseModel
from app.core.security.preauthorize import PreAuthorize
from app.enums.role_enum import RoleEnum
from fastapi import APIRouter, Depends


test = APIRouter(prefix="/test", tags=["Test"])


@test.get("/user", dependencies=[Depends(PreAuthorize(allowed_roles=[RoleEnum.USER, RoleEnum.SUPPORT], strict_roles=True))], response_model=ResponseModel[str],
          response_model_exclude_none=True)
async def user():
    return ResponseModel[str](message="User Dashboard")


@test.get("/admin", dependencies=[Depends(PreAuthorize(allowed_roles=[RoleEnum.ADMIN]))], response_model=ResponseModel[str],
          response_model_exclude_none=True)
async def admin():
    return ResponseModel[str](message="Admin Dashboard")


@test.get("/support", dependencies=[Depends(PreAuthorize(allowed_roles=[RoleEnum.SUPPORT]))], response_model=ResponseModel[str],
          response_model_exclude_none=True)
async def support():
    return ResponseModel[str](message="Support Dashboard")
