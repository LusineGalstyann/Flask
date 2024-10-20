from typing import Annotated, Optional
from fastapi import APIRouter, Depends, UploadFile, File
from database import EmployeeOrm ImageOrm
from schemas import Employee,TaskAdd,TaskResponse


router = APIRouter()




@router.post("/task", tags=["task"])
async def add_task(task:  Task) -> TaskResponse:
    task_id = await TaskRepository.add_one(task)
    return {"id": task_id}


@router.get("/task", tags=["task"])
async def show_all() -> list[TaskAdd]:
    tasks = await TaskRepository.show_all()
    return tasks


@router.post("/upload", tags=["Image"], status_code=201)
async def upload_image(file: UploadFile):
    return await Image.add_image(file)

@router.put("/upload/{id}", tags=["Image"], status_code=201)
async def put_image(id:int, image: ImageModel):
    return await Image.update_image(id,image)

