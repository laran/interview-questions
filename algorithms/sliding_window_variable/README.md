Consider using the sliding window pattern for questions that involve searching 
for a continuous subarray/substring in an array or string that satisfies a 
certain constraint.

If you know the length of the subarray/substring you are looking for, use a 
fixed-length sliding window. Otherwise, use a variable-length sliding window.

Examples:

- Finding the largest substring without repeating characters in a given string
(variable-length).
- Finding the largest substring containing a single character that can be made
by replacing at most k characters in a given string (variable-length).
- Finding the largest sum of a subarray of size k without duplicate elements in
a given array (fixed-length).

Template for any variable length sliding window algorithm:

```python
def variable_length_sliding_window(nums):
	state =  # choose appropriate data structure
	start = 0
	max_ = 0
	
	for end in range(len(nums)):
		# extend window
		# add nums[end] to state in O(1) in time
		
		while state is not valid:
			# repeatedly contract window until it is valid again
			# remove nums[start] from state in O(1) in time
			start += 1
		
		# INVARIANT: state of current window is valid here.
		max_ = max(max_, end - start + 1)
	
	return max_
```