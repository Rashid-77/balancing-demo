from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    pass

# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    pass


# Additional properties to return via API
class User(UserInDBBase):
    pass
