from pymongo import MongoClient

from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

if os.environ.get("MONGODB_URI") is None:
    raise ("MONGODB_URI required to connect to database")

print(f"Connecting to MongoDB {os.environ.get('MONGODB_URI')}")
client = MongoClient(os.environ.get("MONGODB_URI"))

print(client.list_database_names())

db = client["dnd"]

print(db.list_collection_names())
