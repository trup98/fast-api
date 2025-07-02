from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
from db.deps import get_db
from schemas.user_schema import UserCreate, UserOut, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=200)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db, user)
    return {
        "message": "User successfully created",
    }


@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user(db, user_id)
