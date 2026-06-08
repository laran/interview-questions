from typing import List


def max_sum_of_distinct_subarrays(nums: List[int], k: int) -> int:
	"""
	Given an integer array nums and an integer k, write a function to identify
	the highest possible sum of a subarray within nums, where the subarray meets
	the following criteria: its length is k, and all of its elements are unique.
	If no such subarray exists, return 0.
	
	Args:
		nums:
		k:

	Returns:

	Notes:
		See Also: https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k

	"""
	max_sum = float('-inf')
	start = 0
	state = {}
	curr_sum = 0

	for end in range(len(nums)):
		curr_sum += nums[end]
		
		# Increment the counter for nums[end], default to 0.
		state[nums[end]] = state.get(nums[end], 0) + 1

		# If we have a full window, check if all elements are unique and update max_sum.
		if end - start + 1 == k:
			if len(state) == k:
				max_sum = max(max_sum, curr_sum)
			
			# Drop the first element in the window
			curr_sum = curr_sum - nums[start]
			# Decrement the instance counter for nums[start]
			state[nums[start]] = state[nums[start]] - 1
			# Remove the counter for nums[start] when count == 0
			if state[nums[start]] == 0:
				del state[nums[start]]
			# Shift the window
			start += 1
	
	return 0 if max_sum == float('-inf') else max_sum


if __name__ == '__main__':
	assert max_sum_of_distinct_subarrays([3, 2, 2, 3, 4, 6, 7, 7, -1], 4) == 20
	assert max_sum_of_distinct_subarrays([5, 5, 5, 5], 3) == 0
