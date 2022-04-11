from fastapi import APIRouter, File, UploadFile,Depends, HTTPException
from typing import Optional
from models.item import Item
from config.db import client,db
from schemas.item import itemEntity, itemsEntity
from schemas.user import userEntity, usersEntity
from utils import currentUser
import random
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import jwt
import os
from bson.objectid import ObjectId
from dotenv import load_dotenv, find_dotenv

# loads env
load_dotenv(find_dotenv())


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

item = APIRouter()

@item.post('/api/item/createItem')
async def create_post_item(file: UploadFile, item: Optional[str] = None,token: str = Depends(oauth2_scheme)):
    file_location = f"static/files/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    if token:
        user = currentUser(token)
        client.wwear.item.insert_one({"typeOfItem": item, "fileInfpos": file_location,"userId": user["_id"]})
        return {"info": f"file '{file.filename}' saved at '{file_location}'"}
    else: 
        return False

@item.delete('/api/item/deleteItem')
async def delete_post_item(id, token: str = Depends(oauth2_scheme)):
    existItem = client.wwear.item.find_one({"_id": ObjectId(id)})
    if existItem:
        user = currentUser(token)
        ownerItem = client.wwear.item.find_one({"_id": ObjectId(id), "userId": ObjectId(user["_id"])})
        if not ownerItem:
            return {"message : Item not found"}
        else:
            client.wwear.item.delete_one({"_id": ObjectId(id)})
            return {"message : Delete successfully"}
    else:
        return {"message : Item not found"}


@item.get('/api/items')
async def get_all_item():
    return itemsEntity(client.wwear.item.find())

@item.get('/api/items/randoms')
async def get_random_pairs(token: str = Depends(oauth2_scheme)):
    listOfRandom = []
    if token:
        try:
            decode_jwt = currentUser(token)
            now = datetime.now()
            print(decode_jwt)
            print(now)
            user = client.wwear.user.find_one({"userName": decode_jwt["sub"]})
            listPants = await queryListByCats("pants", user["_id"])
            # listShirt = await queryListByCats("shirt", user["_id"])
            listOfRandom = [(random.choice(listPants))]
            return (listOfRandom)
        except jwt.ExpiredSignatureError:
            return False
    else:
        return False

async def queryListByCats(item, userid):
    return itemsEntity(client.wwear.item.find({"typeOfItem": item,"userId":userid}))
