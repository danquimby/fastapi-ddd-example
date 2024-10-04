from sqlalchemy.ext.asyncio import AsyncSession

from app.features.task.domain.repositories.task_repository import TaskRepository
from app.features.task.domain.repositories.task_unit_of_work import TaskUnitOfWork


class TaskUnitOfWorkImpl(TaskUnitOfWork):

    def __init__(self, session: AsyncSession, repository: TaskRepository):
        self.session: AsyncSession = session
        self.repository: TaskRepository = repository

    async def begin(self):
        await self.session.begin()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
