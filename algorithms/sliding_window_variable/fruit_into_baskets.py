from typing import List


def fruit_into_baskets(fruits: List[int]) -> int:
	"""
	Write a function to calculate the maximum number of fruits you can collect
	from an integer array fruits, where each element represents a type of fruit.
	You can start collecting fruits from any position in the array, but you must
	stop once you encounter a third distinct type of fruit. The goal is to find
	the longest subarray where at most two different types of fruits are collected.
	
	Args:
		fruits:

	Returns:
		The length of the longest subarray.

	Notes:
		Time complexity: O(n) we never iterate the array more than once
		Space complexity: O(1) as state never contains more than 3 keys
		
		See Also: https://www.hellointerview.com/learn/code/sliding-window/variable-length

	"""
	start = 0
	state = {}
	max_fruit = 0
	
	for end in range(len(fruits)):
		state[fruits[end]] = state.get(fruits[end], 0) + 1
		
		# Contract lhs as needed
		while len(state) > 2:
			state[fruits[start]] -= 1
			if state[fruits[start]] == 0:
				del state[fruits[start]]
			start += 1
			
		max_fruit = max(max_fruit, end - start + 1)
		
	return max_fruit
	

if __name__ == '__main__':
	assert fruit_into_baskets([3,3,2,1,2,1,0]) == 4