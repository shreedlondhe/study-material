
def test_1():
    x = 10
    y = 20
    assert x == y


def test_2():
    x = 20
    y = 20
    assert x == y


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
