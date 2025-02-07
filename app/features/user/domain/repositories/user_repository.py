from abc import abstractmethod

from app.core.repositories.base_repository import BaseRepository
from app.features.user.domain.entities.user_entity import UserEntity


class UserRepository(BaseRepository[UserEntity]):

    @abstractmethod
    async def find_by_email(self, email: str) -> UserEntity | None:
        raise NotImplementedError()

