from app.persistence.database_config import get_db
from app.persistence.entity.db_entities import UserEntity, RoleEntity
from typing import List
from sqlalchemy import select


class UsuarioRepository:
    def get_roles(self, id: int) -> List[str]:
        with get_db() as db:
            stmt = select(RoleEntity.name).join(RoleEntity.usuarios).filter(UserEntity.id == id)
            return db.execute(stmt).scalars().all()
