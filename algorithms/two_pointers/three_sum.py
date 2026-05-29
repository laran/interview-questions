from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """Find all unique triplets in ``nums`` that sum to zero.

    Sorts the input, then fixes each element ``nums[i]`` and runs a
    two-pointer search over the remainder for a pair summing to
    ``-nums[i]``. Sorting enables both the two-pointer scan and the
    duplicate-skipping that keeps the output free of repeated triplets.

    Note: sorts ``nums`` in place, so the caller's list is mutated.

    Time complexity: O(n^2). Sorting is O(n log n); the outer loop runs n
    times and each iteration's two-pointer scan is O(n), so the nested work
    dominates.

    Space complexity: O(n^2) counting the output, since there can be up to
    O(n^2) distinct triplets (each pair of values fixes the third).
    Auxiliary space excluding the output is O(1) beyond the sort.

    Args:
        nums (List[int]): Integers to search; order is not required (sorted internally).

    Returns:
        List[List[int]]: List of ``[a, b, c]`` triplets with ``a + b + c == 0``, each
        distinct by value, with ``a <= b <= c``.

    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]

    Note:
        See: https://www.hellointerview.com/learn/code/two-pointers/3-sum
    """

    nums.sort()
    result = []

    # Fix the smallest element of each triplet. Stop at len - 2 so there is
    # always room for the left/right pair to its right.
    for i in range(len(nums) - 2):
        # Skip duplicate values of i: an identical nums[i] would only
        # reproduce triplets already found on the previous iteration.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two-pointer search over the sub-array to the right of i, looking
        # for a pair that sums to -nums[i] (i.e. makes the total zero).
        # Reset the window to (i+1, end) fresh for each new i.
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1  # Sum too small: raise it by moving left up.
            elif total > 0:
                right -= 1  # Sum too large: lower it by moving right down.
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Advance both pointers past any duplicates so the next
                # iteration produces a distinct triplet, not a repeat of
                # this one. (This dedup is for left/right; the i-level
                # dedup above is handled separately.)
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Step onto the next pair of candidate values.
                left += 1
                right -= 1

    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -1]) == [[-1, -1, 2], [-1, 0, 1]]
