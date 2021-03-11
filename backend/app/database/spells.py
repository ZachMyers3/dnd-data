from bson.objectid import ObjectId

from .database import db

from typing import List, Dict

from .schema.spells import SpellSchema


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


def insert_spell(spell: SpellSchema) -> SpellSchema:
    return db.spells.insert_one(spell)


def update_spell(spell: SpellSchema) -> SpellSchema:
    return db.spells.update_one({"_id": spell.object_id}, {"$set": spell})


def delete_spell(_id: str):
    return db.spells.delete_one({"_id": _id})
