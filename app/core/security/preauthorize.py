from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import List, Dict, Any
from app.enums.role_enum import RoleEnum
from app.core.jwt import security_jwt
from app.persistence.repository.usuario_repository import UsuarioRepository
from typing_extensions import Annotated, Doc

oauth2_schema = OAuth2PasswordBearer("/api/v1/auth/login")


class PreAuthorize():
    """
    PreAuthorize module based in roles (enums)
    
    #### Example
    
    ```python
    @test.post("/", dependencies=[Depends(PreAuthorize(allowed_roles=[RoleEnum.ADMIN])])
    ```
    
    """
    
    def __init__(
        self, 
        allowed_roles: Annotated[
            List[RoleEnum], 
            Doc(
                """
                List of roles, indicate which roles are authorized.
                """
            )
        ] = None,
        allow_all: Annotated[
            bool, 
            Doc("""
                Boolean indicating all roles are authorized.
                """)
        ] = False, 
        strict_roles: Annotated[
            bool, 
            Doc("""
                Indicates that a user must have strictly the indicated roles, 
                no more roles, or contain the indicated roles.
                """)
        ] = False
        ):
        self.allowed_roles = allowed_roles
        self.allow_all = allow_all
        self.strict_roles = strict_roles
        self.__usuario_repository = UsuarioRepository()
        
    async def __call__(self, token: str = Depends(oauth2_schema)):
        payload: Dict[str, Any] = security_jwt.decode_jwt(token)
        
        if self.allowed_roles is None and not self.allow_all:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nobody can access")
        
        if self.allow_all:
            return True
        
        user_roles: List[str] = self.__usuario_repository.get_roles(payload.get("id"))
        
        allow: bool = all(rol.value in user_roles for rol in self.allowed_roles) if self.strict_roles else \
            any(rol.value in user_roles for rol in self.allowed_roles)

        if not allow:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You can't access")
        