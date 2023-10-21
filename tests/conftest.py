import pytest

from app.services.myservice_impl import MyServiceImpl
from app.services.ports.mydataport import MyDataPort
from app.services.ports.myservice import MyService


class TestDataPort(MyDataPort):
    def save(self, data: str) -> bool:
        return data == "true"


@pytest.fixture(scope="module")
def service() -> MyService:
    return MyServiceImpl(TestDataPort())
