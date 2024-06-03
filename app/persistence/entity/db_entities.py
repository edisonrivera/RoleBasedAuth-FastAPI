from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass



class RoleEntity(Base):
    __tablename__ = 'rol'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)

    usuarios = relationship("UserEntity", secondary="rol_usuario", back_populates="roles")



class UserEntity(Base):
    __tablename__ = 'usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    roles = relationship("RoleEntity", secondary="rol_usuario", back_populates="usuarios")
    


class RoleUserEntity(Base):
    __tablename__ = 'rol_usuario'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey("rol.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"))
