import pytest

from factorial import fact

def test_fact0():
    assert fact(0) == 1


def test_fact1():
    assert fact(3) == 6


def test_fact5():
    assert fact(5) == 120