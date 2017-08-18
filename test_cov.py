import pytest

import fefe

@pytest.fixture
def fe():
    raise Exception

@pytest.fixture
def v():
    raise Exception

def test_c():
    assert False

def test_o(v):
    raise Exception

def test_f():
    assert 2 + 2 == 5

def test_e(fe):
    1 / 0

