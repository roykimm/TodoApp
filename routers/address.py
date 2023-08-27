import sys
sys.path.append("..")

from typing import Optional, Annotated
from fastapi import Depends, APIRouter, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user

router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not Found."}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    postalcode: str
    apt_num: Optional[int]


@router.post("/")
async def create_address(address: Address,
                         user: user_dependency,
                         db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="authentication Failed")
    address_model = models.Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postalcode = address.postalcode
    address_model.apt_num = address.apt_num

    db.add(address_model)
    db.flush()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()

    user_model.address_id = address_model.id
    db.add(user_model)
    db.commit()
