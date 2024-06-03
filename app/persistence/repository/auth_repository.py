from app.persistence.database_config import get_db
from app.persistence.entity.db_entities import UserEntity, RoleEntity
from app.dto.request.register_request import RegisterBaseRequest
from typing import Optional, List


class AuthRepository:
    
    def login(self, nickname: str) -> Optional[UserEntity]:
        with get_db() as db:
            return db.query(UserEntity).filter(UserEntity.nickname == nickname).first()
        
    def register(self, data_user: RegisterBaseRequest, roles: List[RoleEntity]) -> UserEntity:
        with get_db() as db:
            user: UserEntity = UserEntity(**data_user.model_dump(include={"nickname", "password"}))
            user.roles = roles
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
