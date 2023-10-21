from app.services.ports.mydataport import MyDataPort
from app.services.ports.myservice import MyService


class MyServiceImpl(MyService):
    def __init__(self, dataport: MyDataPort) -> None:
        self.dataport = dataport

    async def save(self, data: str) -> bool:
        return await self.dataport.save(data)
