from app import fifth_power
import pytest


# ✅ Basic functionality test
def test_fifth_power_positive():
    assert fifth_power(2) == 32
    assert fifth_power(3) == 243


# ✅ Edge case: zero
def test_fifth_power_zero():
    assert fifth_power(0) == 0


# ✅ Negative numbers
def test_fifth_power_negative():
    assert fifth_power(-2) == -32
    assert fifth_power(-3) == -243


# ✅ Large number test
def test_fifth_power_large():
    assert fifth_power(10) == 100000


# ✅ Invalid input test (should raise error)
def test_fifth_power_invalid_input():
    with pytest.raises(TypeError):
        fifth_power("a")


# ✅ Float input (optional depending on your function design)
def test_fifth_power_float():
    assert fifth_power(2.0) == 32.0