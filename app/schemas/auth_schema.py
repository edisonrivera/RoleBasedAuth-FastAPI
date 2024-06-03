from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class JWTSchema(BaseModel):
    access_token: str
    

class JWTPayload(BaseModel):
    id: int
    iat: int = Field(default_factory=lambda: int(datetime.now().timestamp()))
    exp: int = Field(default_factory=lambda: int((datetime.now() + timedelta(hours=1)).timestamp()))