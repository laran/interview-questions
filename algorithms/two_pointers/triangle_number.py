from typing import List


def triangle_number(nums: List[int]) -> int:
    """Count the number of triplets in nums that can form a valid triangle.

    A triplet (a, b, c) forms a valid triangle if the sum of the two
    smaller sides is greater than the largest side. After sorting, for
    any fixed largest side nums[i], we use two pointers to count all
    valid pairs nums[left] and nums[right] where:

        nums[left] + nums[right] > nums[i]

    Args:
        nums (List[int]): A list of non-negative integers representing side lengths.

    Returns:
        The number of index triplets that can form a valid triangle.

    Example:
        >>> triangle_number([11,4,9,6,15,18])
        10

    Note:
         See Also: https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number
    """

    # Sorting lets us treat nums[i] as the largest side and use two pointers.
    nums.sort()

    count = 0

    # Fix nums[i] as the largest side. We need at least two elements before i.
    for i in range(len(nums) - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            # Since nums is sorted, if nums[left] + nums[right] > nums[i],
            # then every value from left through right - 1 also works with nums[right].
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                # Sum is too small, so move left forward to increase it.
                left += 1

    return count


if __name__ == "__main__":
    assert triangle_number([11, 4, 9, 6, 15, 18]) == 10
