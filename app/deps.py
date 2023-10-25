from app.adapters.memory_dataport import MemoryDataPort
from app.services.myservice_impl import MyServiceImpl
from app.services.ports.myservice import MyService


async def myservice_with_memory_dataport() -> MyService:
    return MyServiceImpl(MemoryDataPort())
