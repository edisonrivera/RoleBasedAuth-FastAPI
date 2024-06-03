from app.model.response_model import ResponseModel
from app.schemas.auth_schema import JWTSchema
from app.service.auth_service import AuthService
from app.dto.request.register_request import RegisterRequest
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends


auth = APIRouter(prefix="/auth", tags=["Auth"])


@auth.post("/login", response_model=ResponseModel[JWTSchema], response_model_exclude_none=True,
           description="Login with nickname and password")
async def login(form: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(AuthService)):
    return auth_service.login(form.username, form.password)

@auth.post("/register", response_model=ResponseModel[str], response_model_exclude_none=True,
           description="Login with nickname and password")
async def login(user: RegisterRequest, auth_service: AuthService = Depends(AuthService)):
    return auth_service.register(user)