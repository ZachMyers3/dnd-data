from bson.objectid import ObjectId

from .database import db

from typing import List, Dict


def retrieve_spells():
    return db.spells.find()


def retrieve_spell(_id: str):
    try:
        _id = ObjectId(_id)
    except:
        return None
    finally:
        return db.spells.find_one({"_id": _id})


def insert_spells(json_list: List[Dict]) -> List[Dict]:
    return db.spells.insert_many(json_list)
