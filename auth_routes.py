from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_session, verify_token
from main import SECRET_KEY, bcrypt_context, ALGORITHM, ACCESS_TOKE_EXPIRE_MINUTES
from schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user_id, token_duration=timedelta(minutes=ACCESS_TOKE_EXPIRE_MINUTES)):
    expire_date = datetime.now(timezone.utc) + token_duration
    dic_info = {"sub": user_id, "exp": expire_date}
    encoded_jwt = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    
    return encoded_jwt

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
        refresh_token = create_token(user.id, token_duration=timedelta(days=7))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }

@auth_router.get("/refresh")
async def use_refresh_token(user: User = Depends(verify_token)):
    access_token = create_token(user.id)
    return {
            "access_token": access_token,
            "token_type": "Bearer"
        }