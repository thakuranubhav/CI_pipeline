import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) ==9 , "Test Failed: Square of 3 should be 9"


def test_cube():
    assert square(2) == 8, "Test Failed: Square of 8 should be 4"
    assert square(3) ==27 , "Test Failed: Square of 27 should be 9"


def test_fifth_power():
    assert square(2) == 8, "Test Failed: Square of 8 should be 4"
    assert square(3) ==27 , "Test Failed: Square of 27 should be 9"


def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")