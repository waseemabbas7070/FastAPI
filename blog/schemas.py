from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True
class ShowUser(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: Optional[ShowUser] = None

    class Config:
        orm_mode = True