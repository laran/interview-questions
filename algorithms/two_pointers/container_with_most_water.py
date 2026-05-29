from typing import List


def container_with_most_water(heights: List[int]) -> int:
    """Find the maximum water area between two vertical lines.

    Given an array where each element is the height of a vertical line at
    that index, find two lines that, together with the x-axis, form a
    container holding the most water. Area is bounded by the shorter line,
    so area = (right - left) * min(heights[left], heights[right]).

    Uses the two-pointer technique: start at both ends and move the pointer
    at the shorter line inward, since the shorter line is the binding
    constraint and moving the taller one can never increase the area.

    Args:
        heights (List[int]): Heights of the vertical lines, indexed by position.

    Returns:
        int: Maximum area of water the container can hold.

    Example:
        >>> container_with_most_water([3, 4, 1, 2, 2, 4, 1, 3, 2])
        21

    Note:
         See Also: https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water
    """
    left, right, max_area = 0, len(heights) - 1, 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height

        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    assert container_with_most_water([3, 4, 1, 2, 2, 4, 1, 3, 2]) == 21
