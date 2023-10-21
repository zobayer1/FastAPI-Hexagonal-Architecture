from abc import ABC, abstractmethod


class MyDataPort(ABC):
    @abstractmethod
    async def save(data: str) -> bool:
        pass
