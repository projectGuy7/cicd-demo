"""
Tests for the calculator module.
These run automatically via GitHub Actions on every push!
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.calculator import add, subtract, multiply, divide, power

class TestAddition:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_add_zero(self):
        assert add(5, 0) == 5

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtraction:
    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_resulting_negative(self):
        assert subtract(3, 10) == -7

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiplication:
    def test_multiply_positive(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(7, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-3, 4) == -12


class TestDivision:
    def test_divide_positive(self):
        assert divide(10, 2) == 5.0

    def test_divide_floats(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        """This ensures our error handling works correctly."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)


class TestPower:
    def test_power_positive(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5
