import sys
import pytest


@pytest.mark.smoke
def test_1():
    x = 10
    y = 20
    assert x == y


@pytest.mark.regression
def test_2():
    print(sys.version_info)
    x = 20
    y = 20
    assert x == y


@pytest.mark.regression
@pytest.mark.smoke
def testing_t3():
    x = 10
    y = 20
    result = x + y
    assert result == 40


def pass_testing_t3():      # invalid test function name
    x = 10
    y = 20
    result = x + y
    assert result == 30


def pass_test():      # invalid test function name
    x = 10
    y = 20
    result = x + y
    assert result == 30


@pytest.mark.Prachi
def test_login():
    x = 20
    y = 20
    assert x == y


@pytest.mark.smoke
def test_check_in():
    name = "Credence"
    message = "Credence is the best class in world..."
    assert name in message


@pytest.mark.regression
def test_check_is():
    name = "Credence"
    message = "Credence"
    assert name is message
