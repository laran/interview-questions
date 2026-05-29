from typing import List


def max_subarray_sum(nums: List[int], k) -> float:
	"""Return the maximum sum of any contiguous subarray of length k.

	Uses a fixed-size sliding window: maintain a running sum of the current
	window, and at each full window compare against the running maximum
	before sliding one element right.

	Args:
	    nums: The list of integers to scan.
	    k: The window size. Must satisfy 1 <= k <= len(nums).

	Returns:
	    The maximum sum over all length-k contiguous subarrays.

	Raises:
	    ValueError: If k is not in the range 1 to len(nums).
	"""
	if not 1 <= k <= len(nums):
		raise ValueError(f"k must be between 1 and {len(nums)}, got {k}")
	
	max_sum = float('-inf')
	state = 0
	start = 0
	
	for end in range(len(nums)):
		# Slide the window to include the next element to the right.
		# Given that we start at end = 0, until we fill the full window this
		# just adds the current element to state.
		state += nums[end]
		
		# Once we reach a full window, check the sum against max and slide the
		# window one element to the right.
		if end - start + 1 == k:
			# Check for a new max.
			max_sum = max(max_sum, state)
			
			# Effectively remove the current start value so we can add the
			# next value in the next iteration while keeping the fixed window size.
			state -= nums[start]
			
			# Increment the LHS of the window
			start += 1
	
	return max_sum


if __name__ == '__main__':
	assert max_subarray_sum([2, 1, 5, 1, 3, 2], 3) == 9