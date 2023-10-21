from abc import ABC, abstractmethod


class MyService(ABC):
    @abstractmethod
    async def save(data: str) -> bool:
        pass
