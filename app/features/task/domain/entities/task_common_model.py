from pydantic import Field, BaseModel


class TaskBaseModel(BaseModel):
    title: str = Field(example='Описание задачи')
    owner_id: int = Field(example=1)
