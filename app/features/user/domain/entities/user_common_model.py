from pydantic import BaseModel, Field


class UserBaseModel(BaseModel):
    email: str = Field(example='test@test.com')
