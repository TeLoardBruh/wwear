from fastapi import APIRouter, File, UploadFile, Depends, HTTPException
from typing import Optional
from models.user import User
from config.db import client,db
from schemas.user import userEntity, usersEntity
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv, find_dotenv

# loads env
load_dotenv(find_dotenv())


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
user = APIRouter()

# hashing for password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def getPassword(password):
    return pwd_context.hash(password)

@user.post('/api/user/signup')
async def signup(userName: str, password: str):
    existUser = client.wwear.user.find_one({"userName": userName})
    if existUser:
        raise HTTPException(status_code=400, detail="User name "+userName+" already exist")
    else:
        hashPassword = getPassword(password)
        client.wwear.user.insert_one({"userName": userName, "password": hashPassword})
        return "Sign Up successfully"


# login and get User Information

def authenticate_user(userName, password):
    user = client.wwear.user.find_one({"userName": userName})
    if user:
        password_verify = pwd_context.verify(password, user['password'])
        return password_verify
    else:
        return False

# create access token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@user.post('/token')
async def login(formData: OAuth2PasswordRequestForm = Depends()):
    userName = formData.username
    password = formData.password
    if authenticate_user(userName, password):
        access_token = create_access_token(
            data={"sub":userName}, expires_delta=timedelta(minutes=30)
        )
        return {"access_token": access_token, "token_type":"bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect User name or Password")

    # pass

@user.get('/api/user/me')
async def getMe(token: str = Depends(oauth2_scheme)):
    test = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return {"token": token, "test": test['sub']}
