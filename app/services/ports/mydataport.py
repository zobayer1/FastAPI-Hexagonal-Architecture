from abc import ABC, abstractmethod


class MyDataPort(ABC):

    @abstractmethod
    def save(data: str) -> bool:
        pass
