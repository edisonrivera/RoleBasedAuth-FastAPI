from app.model.response_model import ResponseModel
from app.dto.request.register_request import AdminRegisterRequest
from app.core.security.preauthorize import PreAuthorize
from app.enums.role_enum import RoleEnum
from app.service.admin_service import AdminService

from fastapi import APIRouter, Depends

admin = APIRouter(prefix="/admin", tags=["Admin"])


@admin.post("/register", dependencies=[Depends(PreAuthorize(allowed_roles=[RoleEnum.ADMIN]))], response_model=ResponseModel[str], response_model_exclude_none=True, 
            description="Register new user")
async def register(user: AdminRegisterRequest, admin_service: AdminService = Depends(AdminService)):
    return admin_service.register(user)
