from app.adapters.memory_dataport import MemoryDataPort
from app.services.myservice_impl import MyServiceImpl


async def myservice_with_memory_dataport():
    return MyServiceImpl(MemoryDataPort())
