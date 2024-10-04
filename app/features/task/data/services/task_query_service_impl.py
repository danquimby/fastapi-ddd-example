from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.features.task.data.models.task import Task
from app.features.task.domain.entities.task_query_model import TaskReadModel
from app.features.task.domain.services.task_query_service import TaskQueryService


class TaskQueryServiceImpl(TaskQueryService):

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def find_by_id(self, id_: int) -> TaskReadModel | None:
        result = await self.session.get(Task, id_)

        if result is None:
            return None

        return result.to_read_model()

    async def findall(self) -> Sequence[TaskReadModel]:
        statement = select(Task)

        result = await (self.session.execute(statement)).scalars().all()

        if len(result) == 0:
            return []

        return [task.to_read_model() for task in result]
