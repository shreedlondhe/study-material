import pytest


@pytest.fixture
def setup():
    print("Get driver")
    print("Maximize window")
    yield
    print("print title")
    print("close window")


def test_1(setup):
    print("Open URL of facebook")


def test_2(setup):
    print("Open URL of gmail")


def test_3(setup):
    print("Open URL of Amazon")
