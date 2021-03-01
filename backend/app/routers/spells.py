from typing import List
from bson.objectid import ObjectId
import pathlib
import json


from fastapi import Depends, APIRouter, HTTPException, File, UploadFile

from ..schema.spells import SpellSchema

from ..database.spells import retrieve_spell, retrieve_spells

router = APIRouter()


@router.get("/spells/", response_model=List[SpellSchema])
def get_all_spells():
    return list(retrieve_spells())


@router.get("/spells/{_id}/", response_model=SpellSchema)
def get_spell_by_id(_id: str):
    result = retrieve_spell(_id=_id)
    if result is None:
        HTTPException(status_code=404, detail="Object not found")
    return result


@router.post("/spells/", response_model=List[SpellSchema])
def create_spells_from_file(file: UploadFile = File(...)):
    if file.content_type != "application/json":
        return HTTPException(422, detail="Must be a JSON file")

    json_str = ""
    for line in file.file:
        json_str += line.decode("utf-8")

    json_dict = json.loads(json_str)
    print(json_dict)
