from abc import ABC, abstractmethod

from app.services.ports.mydataport import MyDataPort


class MyService(ABC):
    @abstractmethod
    def save(data: str) -> bool:
        pass
