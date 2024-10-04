from sqlalchemy.ext.asyncio import AsyncSession

from app.features.user.domain.repositories.user_repository import UserRepository
from app.features.user.domain.repositories.user_unit_of_work import UserUnitOfWork


class UserUnitOfWorkImpl(UserUnitOfWork):

    def __init__(self, session: AsyncSession, user_repository: UserRepository):
        self.session: AsyncSession = session
        self.repository: UserRepository = user_repository

    async def begin(self):
        await self.session.begin()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
