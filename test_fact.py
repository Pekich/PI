import pytest

from main import fact

def test_fact0():
    assert fact(0) == 1


def test_fact1():
    assert fact(1) == 1


def test_fact5():
    assert fact(5) == 120
