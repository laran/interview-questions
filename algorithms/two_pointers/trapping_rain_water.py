from typing import List


def trapping_rain_water(heights: List[int]) -> int:
	"""
	Write a function to calculate the total amount of water trapped between bars
	on an elevation map, where each bar's width is 1. The input is given as an
	array of n non-negative integers height representing the height of each bar.
	
	This algorithm does not require heights to be sorted (as it typical for
	two-pointers problems). But the
	
	Args:
		height:

	Returns:
		The total amount of water trapped between bars.

	Notes:
		See Also: https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water

	"""
	if not heights:
		return 0
	
	left, right = 0, len(heights) - 1
	left_max, right_max = heights[left], heights[right]
	count = 0
	
	while left < right: # Stop when left and right cross
		if left_max < right_max:
			# When left_max < right_max we know that water is trapped on the
			# right because right_max >= left_max, so we work on the left side.
			left += 1
			if heights[left] >= left_max:
				left_max = heights[left]
			else:
				count += left_max - heights[left]
		else:
			# When left_max >= right_max we know that water is trapped on the
			# left because right_max < left_max, so we work on the right side.
			right -= 1
			if heights[right] >= right_max:
				right_max = heights[right]
			else:
				count += right_max - heights[right]
				
	return count


if __name__ == "main":
	assert trapping_rain_water([3, 4, 1, 2, 2, 5, 1, 0, 2]) == 10
