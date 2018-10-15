from questions.spiral_array import *


def arrays_are_equal(a, b):
    """
    Check that two multi-dimensional arrays of ints are equivalent

    :param a:
    :param b:
    :return:
    """
    if a is None and b is None:
        return True

    if type(a) == list and type(b) == list:
        if len(a) == 0 and len(b) == 0:
            return True
        else:
            return all(arrays_are_equal(a[i], b[i]) for i in range(len(a) - 1))
    elif type(a) == int and type(b) == int:
        return a == b
    else:
        raise Exception("Only ints and lists are allowed. Found {}".format(type(a)))


def test_shouldHandleZero():
    assert arrays_are_equal(spiralize(0), [])


def test_shouldHandleOne():
    assert arrays_are_equal(spiralize(1), [[1]])


def test_shouldHandleEvenNumbers():
    assert arrays_are_equal(spiralize(2), [[1, 2], [4, 3]])


def test_shouldHandleOddNumbers():
    assert arrays_are_equal(spiralize(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
