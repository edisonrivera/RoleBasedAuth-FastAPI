from pydantic import BaseModel, field_validator, ConfigDict
from fastapi import HTTPException, status
from app.validator import password_validator
from app.util import password_util
from typing import List



class RegisterBaseRequest(BaseModel):
    nickname: str
    password: str
    
    model_config = ConfigDict(
        extra="forbid"
    )
    
    @field_validator("nickname")
    def validate_nickname(cls, nickname: str) -> str:
        MAX_LEN_NICKNAME: int = 50
        MIN_LEN_NICKNAME: int = 3
        if not MIN_LEN_NICKNAME < len(nickname) < MAX_LEN_NICKNAME:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid nickname")

        return nickname.strip()
    
    @field_validator("password")
    def password_validator(cls, password: str):
        if not password_validator.is_valid_password(password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="La contraseña no cumple con los requisitos necesarios")

        return password_util.encrypt_password(password)
    
    
    
class RegisterRequest(RegisterBaseRequest):
    pass



class AdminRegisterRequest(RegisterBaseRequest):
    roles: List[int]
