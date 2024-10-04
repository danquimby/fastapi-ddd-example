from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.user.data.models.user import User
from app.features.user.domain.entities.user_query_model import UserReadModel
from app.features.user.domain.services.user_query_service import UserQueryService


class UserQueryServiceImpl(UserQueryService):
    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: int) -> UserReadModel | None:
        result = await self.session.get(User, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[UserReadModel]:
        statement = select(User).filter_by(is_deleted=False)

        result = await (self.session.execute(statement)).scalars().all()

        return [user.to_read_model() for user in result]
