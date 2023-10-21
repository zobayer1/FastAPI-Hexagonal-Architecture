from typing import Any

from fastapi import Depends, FastAPI, Query
from app.deps import myservice_with_memory_dataport

app = FastAPI(title="Hexagonal")


@app.put("/")
async def save_data(data=Query(), service=Depends(myservice_with_memory_dataport)) -> Any:
    return await service.save(data)
