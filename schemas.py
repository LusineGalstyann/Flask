from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel


class TaskAdd(Task):
    id: int

class ImageModel(BaseModel):
    name:str | None = None
    data:str|None = None

class ImageModelId(ImageModel):
    id:int

class TaskResponse(BaseModel):
    id: int
