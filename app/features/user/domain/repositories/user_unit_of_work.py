from app.core.unit_of_work.unit_of_work import AbstractUnitOfWork
from app.features.user.domain.repositories.user_repository import UserRepository


class UserUnitOfWork(AbstractUnitOfWork[UserRepository]):
    pass
