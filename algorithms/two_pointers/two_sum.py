from typing import List


def two_sum(sorted_nums: List[int], target: int) -> List[int] | None:
    """Find indices of two values in a sorted array that sum to a target.

    Assumes ``arr`` is sorted in ascending order. Uses two pointers from
    both ends: if the current sum is too small, advance the left pointer to
    increase it; if too large, retreat the right pointer to decrease it.
    This works precisely because the array is sorted.

    Args:
        sorted_nums (List[int]): Ascending-sorted sequence of numbers.
        target (int): Sum to search for.

    Returns: ``[left, right]`` indices of the matching pair, or ``None`` if
        no pair sums to the target.

    Example:
        >>> two_sum([1, 2, 3, 4, 5], 7)
        [1, 4]

    Note:
         See Also: https://www.hellointerview.com/learn/code/two-pointers/two-sum
    """
    left, right = 0, len(sorted_nums) - 1

    while left < right:
        tmp_sum = sorted_nums[left] + sorted_nums[right]
        if tmp_sum == target:
            return [left, right]
        elif tmp_sum < target:
            left += 1
        else:
            right -= 1

    return None


if __name__ == "__main__":
    assert two_sum([1, 2, 3, 4, 5], 7) == [1, 4]
