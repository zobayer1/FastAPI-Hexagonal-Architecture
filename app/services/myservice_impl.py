from fastapi import Depends
from app.adapters.memory_dataport import MemoryDataPort
from app.services.ports.mydataport import MyDataPort
from app.services.ports.myservice import MyService


class MyServiceImpl(MyService):

    def __init__(self, dataport: MyDataPort = Depends(MemoryDataPort)) -> None:
        self.dataport = dataport

    def save(self, data: str) -> bool:
        return self.dataport.save(data)
