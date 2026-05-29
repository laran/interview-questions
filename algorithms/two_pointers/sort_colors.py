from typing import List

from array_utils import swap


def sort_colors(nums: List[int]) -> None:
    """Sort an array of 0s, 1s, and 2s in place.

    Write a function to sort a given integer array nums in-place (and without
    the built-in sort function), where the array contains n integers that are
    either 0, 1, and 2 and represent the colors red, white, and blue. Arrange
    the objects so that same-colored ones are adjacent, in the order of red,
    white, and blue (0, 1, 2).

    Using a 3-pointer approach, we can define the following invariants:
    1. All elements to the left of `left` are 0s.
    2. All elements between `left` and `i -1` are 1s.
    3. All elements between `i` and `right` are unsorted.
    4. All elements to the right of `right` are 2s.

    Notes:
        See: https://www.hellointerview.com/learn/code/two-pointers/sort-colors

    """

    i, left, right = 0, 0, len(nums) - 1

    while i <= right:
        if nums[i] == 0:
            swap(nums, i, left)
            left += 1
            i += 1
        elif nums[i] == 2:
            swap(nums, i, right)
            right -= 1
        else:
            i += 1


if __name__ == "__main__":
    example = [2, 1, 2, 0, 1, 0, 1, 0, 1]
    sort_colors(example)
    assert example == [0, 0, 0, 1, 1, 1, 1, 2, 2]
