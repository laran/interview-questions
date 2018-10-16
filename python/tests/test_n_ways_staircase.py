from n_ways_staircase import ways_to_climb

"""
Test with sizes small enough that I can do the math in my head
"""


def test_shouldWorkWith3StepsAndMaxStepSizeOf3():
    assert ways_to_climb(3, 3) == 4


def test_shouldWorkWith3StepsAndMaxStepSizeOf2():
    assert ways_to_climb(3, 2) == 3


def test_shouldWorkWith4StepsAndMaxStepSizeOf2():
    assert ways_to_climb(4, 2) == 5
