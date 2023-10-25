from typing import Any

from fastapi import Depends, FastAPI, Query
from app.deps import myservice_with_memory_dataport
from app.services.ports.myservice import MyService

app = FastAPI(title="Hexagonal")


@app.put("/")
async def save_data(data: str = Query(), service: MyService = Depends(myservice_with_memory_dataport)) -> Any:
    return await service.save(data)
