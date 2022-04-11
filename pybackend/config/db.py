from enum import unique
import pymongo
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_URL = os.getenv("DB_URL")

client = pymongo.MongoClient(DB_URL)
db = client.test
print(db)
