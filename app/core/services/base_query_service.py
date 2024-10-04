from abc import ABC, abstractmethod
from typing import Sequence, TypeVar, Generic

_T = TypeVar('_T')

class QueryService(ABC, Generic[_T]):

    @abstractmethod
    async def find_by_id(self, id_: int) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    async def findall(self) -> Sequence[_T]:
        raise NotImplementedError()
