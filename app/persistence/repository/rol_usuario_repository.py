from app.persistence.database_config import get_db
from app.persistence.entity.db_entities import RoleUserEntity
from typing import List


class RolUsuarioRepository:
    def get_all_by_id(self, usuario_id: int) -> List[RoleUserEntity]:
        with get_db() as db:
            return db.query(RoleUserEntity).filter(RoleUserEntity.usuario_id == usuario_id).all()
            