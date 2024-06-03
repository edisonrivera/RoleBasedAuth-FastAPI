from app.persistence.database_config import get_db
from app.persistence.entity.db_entities import RoleEntity
from app.enums.role_enum import RoleEnum


class RolRepository:
    def map_roles_by_name(self, role: RoleEnum) -> RoleEntity:
        with get_db() as db:
            return db.query(RoleEntity).filter(RoleEntity.name == role.value).first()
        
    def map_roles_by_id(self, id_rol: int) -> RoleEntity:
        with get_db() as db:
            return db.query(RoleEntity).filter(RoleEntity.id == id_rol).first()
                