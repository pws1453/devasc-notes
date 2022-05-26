import maths
import pytest

def test_algebra():
    res = maths.add1(1)
    assert res == 2

def test_circle():
    res = maths.circumference(2)
    assert res == 12.56
