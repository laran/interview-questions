from typing import List


def swap(nums: List[int], i: int, j: int) -> None:
    """Swap the elements at indices i and j in place.

    Args:
        nums: The list to modify. Mutated in place.
        i: Index of the first element.
        j: Index of the second element.

    Note:
        Written in three-line tmp form rather than the idiomatic
        ``nums[i], nums[j] = nums[j], nums[i]``. The tuple form is
        correct and needs no temp (Python evaluates the whole right
        side before assigning), but the explicit form keeps the swap
        mechanically identical to its Java equivalent, which has no
        one-line tuple swap.
    """
    tmp = nums[j]
    nums[j] = nums[i]
    nums[i] = tmp
