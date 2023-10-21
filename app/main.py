from fastapi import Depends, FastAPI, Query
from app.services.myservice_impl import MyServiceImpl

app = FastAPI(title="Hexagonal")


@app.put("/")
def save_data(data=Query(), service=Depends(MyServiceImpl)) -> bool:
    return service.save(data)
