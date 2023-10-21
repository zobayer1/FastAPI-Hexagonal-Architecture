import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize("input,expected", [("true",True), ("false", False), ("somethingelse", False)])
async def test_save_succeeds(input, expected, service):
    assert await service.save(input) == expected
