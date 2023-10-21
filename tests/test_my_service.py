import pytest

@pytest.mark.parametrize("input,expected", [("true",True), ("false", False), ("somethingelse", False)])
def test_save_succeeds(input, expected, service):
    assert service.save(input) == expected
