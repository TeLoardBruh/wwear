from jose import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def currentUser(token):
    currentUser = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return currentUser