from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud, schemas
from api import deps
from subprocess import check_output

ips = check_output(['hostname', '--all-ip-addresses'])
router = APIRouter()

#---------------------------------------------------------------
#---------------------------------------------------------------

@router.post("/register", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="A user with same username already exists.",
        )
    return crud.user.create(db, obj_in=user_in)


@router.get("/{user_id}")
def read_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"host": ips, "user": user.username}
