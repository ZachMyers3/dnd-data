from bson.objectid import ObjectId

from .database import db

from typing import List, Dict

from ..schema.spells import SpellSchema


def retrieve_spells():
    return db.spells.find()


def retrieve_spell(_id: str):
    try:
        _id = ObjectId(_id)
    except Exception:
        return None
    finally:
        return db.spells.find_one({"_id": _id})


def insert_spells(json_list: List[Dict]) -> List[Dict]:
    return db.spells.insert_many(json_list)


def insert_spell(spell: dict) -> SpellSchema:
    return db.spells.insert_one(spell)


def update_spell(spell: dict) -> SpellSchema:
    update_id = ObjectId(spell["_id"])
    del spell["_id"]
    return db.spells.update_one(
        {"_id": update_id}, {"$set": spell}
    )


def delete_spell(_id: str):
    _id = ObjectId(_id)
    return db.spells.delete_one({"_id": _id})
