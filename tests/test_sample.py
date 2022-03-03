def is_even(x: int) -> bool:
    if x % 2 == 0:
        return True
    else:
        return False


def test_is_even():
    assert is_even(2) is False
    assert is_even(2) is True
