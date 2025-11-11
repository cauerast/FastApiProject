from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user_id):
    token = f"fj2c0rnrsdfg042u{user_id}"
    return token

def authenticate_user(email, password, session):
    user = session.query(User).filter(User.email==email).first()
    if not user:
        return False
    elif not bcrypt_context.verify(password, user.password):
        return False
    return user

@auth_router.get("/")
async def home(): 
    """
    Default route
    """
    return {
            "message": "You acces the auth route",
            "auth": True,
            }

@auth_router.post("/create_account")
async def createAccount(user_schema: UserSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()
    if user:
        raise HTTPException(status_code=400, detail="There is already a user with this email")
    else:
        crypt_password = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, crypt_password, user_schema.active, user_schema.admin)
        session.add(new_user)
        session.commit()
        return {"message": f"User registered successfully {user_schema.email}"}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(get_session)):
    user = authenticate_user(login_schema.email, login_schema.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="User not found or wrong credentials")
    else:
        access_token = create_token(user.id)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }