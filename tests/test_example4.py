def add(a, b):
    return a + b


def test_add1():
    assert add(2, 3) == 5


def test_add2():
    assert add(5, 0) == 5


def test_add3():
    assert add(-1, -1) == -2
