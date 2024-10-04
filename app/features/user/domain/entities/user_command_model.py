from pydantic import Field, BaseModel

from app.features.user.domain.entities.user_common_model import UserBaseModel


class UserCreateModel(UserBaseModel):
    password: str = Field(example='password')


class UserUpdateModel(BaseModel):
    email: str | None
    password: str | None = Field(example='password')
    is_active: bool | None = Field(example=True)
    is_deleted: bool | None = Field(example=True)
