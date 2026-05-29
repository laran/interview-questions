def max_subarray_sum(nums, k) -> float:
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