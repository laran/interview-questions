from typing import List

from array_utils import swap


def move_zeroes(nums: List[int]) -> None:
    """Move all zeros to the end, preserving non-zero order, in place.

    Uses two pointers. The lead pointer (``scanner``) looks ahead for
    the next non-zero value; the trailing pointer (``next_non_zero``)
    marks the slot the next non-zero element should occupy. The gap
    between them equals the number of zeros seen so far.

    Args:
        nums: The list to modify. Mutated in place; no copy is made.

    Note:
        When the input has no zeros, or leading non-zero elements,
        each such element is swapped with itself (a no-op, since
        ``scanner == next_non_zero`` until the first zero is seen).
        Guarding with ``if scanner != next_non_zero`` would avoid the
        redundant swap, but trades a cheap swap for a cheap comparison
        and isn't worth it unless writes are genuinely expensive.

        Reference:
        https://www.hellointerview.com/learn/code/two-pointers/move-zeroes
    """
    next_non_zero = 0

    for scanner in range(len(nums)):
        if nums[scanner] != 0:
            swap(nums, next_non_zero, scanner)
            next_non_zero += 1


if __name__ == "__main__":
    example = [2, 0, 4, 0, 9]
    move_zeroes(example)
    assert example == [2, 4, 9, 0, 0]
