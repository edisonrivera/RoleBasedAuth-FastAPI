from app.core.config.env_variables import get_env_vars
from app.schemas.auth_schema import JWTPayload, JWTSchema
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Dict, Any

env = get_env_vars()
oauth2_schema = OAuth2PasswordBearer("/api/v1/auth/login")


def sign_jwt(payload: JWTPayload) -> JWTSchema:
    return JWTSchema(access_token=jwt.encode(payload.model_dump(), env.JWT_SECRET, algorithm=env.ALGORITHM))

def decode_jwt(token: str = Depends(oauth2_schema)) -> Dict[str, Any]:
    try:
        if not token:
            raise HTTPException(status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, 
                                detail="Token not exists")
            
        return jwt.decode(token, env.JWT_SECRET, algorithms=[env.ALGORITHM])
        
    except ExpiredSignatureError:
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Token Expired")      
            
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="Invalid Token")
        
        