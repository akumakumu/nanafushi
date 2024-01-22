from dotenv import load_dotenv
import os

from pymongo import MongoClient

load_dotenv()

myURI = os.getenv('URI')
myPORT = os.getenv('PORT')
myDB = os.getenv('DB')

client = MongoClient(myURI, int(myPORT))

db = client[myDB]

for i in db.yytestdb.find():
    print(i)