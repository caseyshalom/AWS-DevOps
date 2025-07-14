#Next, add the test with PyTest.

import pytest
from calc_functions import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0

def test_subtract():
    value = subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0

def test_multiply():
    value = multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    value = divide(NUMBER_1, NUMBER_2)
    assert value == 1.5