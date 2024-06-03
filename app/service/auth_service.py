from app.model.response_model import ResponseModel
from app.core.jwt import security_jwt
from app.schemas.auth_schema import JWTPayload, JWTSchema
from app.util import password_util
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException, status
from app.enums.role_enum import RoleEnum
from sqlalchemy.exc import DatabaseError
from app.persistence.repository.auth_repository import AuthRepository
from app.persistence.repository.rol_repository import RolRepository
from app.persistence.entity.db_entities import UserEntity, RoleEntity
from app.dto.request.register_request import RegisterRequest
from sqlalchemy.exc import DatabaseError



class AuthService(BaseModel):
    __auth_repository: AuthRepository = AuthRepository()
    __rol_repository: RolRepository = RolRepository()
    
    def login(self, nickname: str, password: str) -> ResponseModel[JWTSchema]:
        try:
            user: Optional[UserEntity] = self.__auth_repository.login(nickname)
            
            if user is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            
            if not password_util.check_password(password, user.password):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Password")
            
            return ResponseModel[JWTSchema](
                message="Login Successfully",
                data=security_jwt.sign_jwt(
                    JWTPayload(id=user.id)
                )
            )
            
        except DatabaseError:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Password")
            
        
    def register(self, user_register: RegisterRequest) -> ResponseModel[str]:
        try:
            roles: List[RoleEntity] = [self.__rol_repository.map_roles_by_name(rol) for rol in [RoleEnum.ADMIN]]
            user_saved: UserEntity = self.__auth_repository.register(user_register, roles)
            return ResponseModel[str](message=f"User {user_saved.nickname} registered successfully")
        
        except DatabaseError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error to register user") from e