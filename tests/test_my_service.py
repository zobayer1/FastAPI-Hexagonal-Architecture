import pytest

from app.services.ports.myservice import MyService


@pytest.mark.asyncio
@pytest.mark.parametrize("input,expected", [("true",True), ("false", False), ("somethingelse", False)])
async def test_save_succeeds(input: str, expected: bool, service: MyService) -> None:
    assert await service.save(input) == expected
