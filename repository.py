import pytesseract
from fastapi import UploadFile, HTTPException
from PIL import Image
from database import new_session


class TaskRepository:
    @classmethod
    async def add_one(cls, data: Task) -> int:
        async with new_session() as session:
            data_dic = data.model_dump()
            task = TaskOrm(**data_dic)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def show_all(cls) -> list[TaskAdd]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [TaskAdd.model_validate(task.__dict__) for task in task_models]
            return task_schemas


class Image:
    @classmethod
    async def add_image(cls, file: UploadFile) -> ImageOrm:
        async with new_session() as session:
            text = pytesseract.image_to_string(img.open(file.file))
            file_name = file.filename
            data = ImageOrm(data=text, name=file_name)
            session.add(data)
            await session.flush()
            await session.commit()
            return data

