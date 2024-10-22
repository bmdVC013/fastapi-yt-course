from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


class UserBase(BaseModel):
  id: int
  email: EmailStr
  created_at: datetime

  class Config:
    from_attributes = True

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class UserOut(UserBase):
  pass

class UserIn(BaseModel):
  email: EmailStr
  password: str

class PostBase(BaseModel):
  id: int
  title: str
  content: str
  published_at: Optional[datetime] = None
  created_at: datetime
  owner_id: int
  owner: UserOut

  class Config:
    from_attributes = True

class PostIn(BaseModel):
  title: str
  content: str

class PostOut(BaseModel):
  Post: PostBase
  total_votes: int

  class Config:
    from_attributes = True

class VoteBase(BaseModel):
  post_id: int
  user_id: int

class VoteIn(BaseModel):
  post_id: int
  dir: conint(le=1) # type: ignore

class TokenBase(BaseModel):
  id: Optional[str] = None

class TokenOut(BaseModel):
  access_token: str
  token_type: str