from typing import Optional

from pydantic import BaseModel


class UserId(BaseModel):
    id: Optional[int] = None


class UserBase(BaseModel):
    username: Optional[str] = None


class UserCreate(UserBase):
    pass

class UserToDB(UserId, UserCreate):
    pass


class UserInDB(UserToDB):
    pass


# Additional properties to return via API
class User(UserBase, UserId):
    pass
