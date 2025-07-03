from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status
from crud import user_crud
from db.deps import get_db
from schemas.user_schema import UserCreate, UserUpdate, UserOut
from schemas.response_schema import ApiResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=ApiResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_crud.create_user(db, user)
    return ApiResponse(
        status=status.HTTP_201_CREATED,
        message="User successfully created",
        data=None
    )


@router.get("/", response_model=None)
def list_users(db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db)
    return ApiResponse(
        status=status.HTTP_200_OK,
        message="Users found successfully",
        data=[UserOut.from_orm(user).dict() for user in users]
    )


@router.get("/{user_id}", response_model=ApiResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_id(db, user_id)
    return ApiResponse(
        status=status.HTTP_200_OK,
        message="User found successfully",
        data=db_user
    )


@router.put("/{user_id}", response_model=ApiResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    user_crud.update_user(db, user_id, user)
    return ApiResponse(
        status=status.HTTP_200_OK,
        message="User updated successfully",
        data=None
    )


@router.delete("/{user_id}", response_model=ApiResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_crud.delete_user(db, user_id)
    return ApiResponse(
        status=status.HTTP_200_OK,
        message="User Deleted successfully",
        data=None
    )
