from app.model.response_model import ResponseModel
from pydantic import BaseModel
from typing import Optional, List
from fastapi import HTTPException, status
from sqlalchemy.exc import DatabaseError
from app.persistence.repository.auth_repository import AuthRepository
from app.persistence.repository.rol_repository import RolRepository
from app.persistence.entity.db_entities import UserEntity, RoleEntity
from app.dto.request.register_request import AdminRegisterRequest
from sqlalchemy.exc import DatabaseError



class AdminService(BaseModel):
    __auth_repository: AuthRepository = AuthRepository()
    __rol_repository: RolRepository = RolRepository()
    
    def register(self, user: AdminRegisterRequest) -> ResponseModel[str]:
        try:
            roles: List[RoleEntity] = []
            for id_rol in user.roles:
                rol: Optional[RoleEntity] = self.__rol_repository.map_roles_by_id(id_rol)
                if rol is None:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role not found")
                roles.append(rol)
                
            user_saved: UserEntity = self.__auth_repository.register(user, roles)
            return ResponseModel[str](message=f"User {user_saved.nickname} registered successfully")
        
        except DatabaseError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error to register user") from e