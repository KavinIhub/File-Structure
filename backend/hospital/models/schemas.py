from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, Annotated
from datetime import datetime
from bson import ObjectId

# Simple ObjectId type annotation for Pydantic v2
PyObjectId = Annotated[str, Field(description="MongoDB ObjectId")]

# User Models
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=2, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=100)

class UserLogin(BaseModel):
    username: str
    password: str

class UserInDB(UserBase):
    id: PyObjectId = Field(default="", alias="_id")
    hashed_password: str
    is_active: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: Optional[datetime]
    
    model_config = ConfigDict(from_attributes=True)

# Token Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Response Models
class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class MessageResponse(BaseModel):
    message: str
    success: bool = True
