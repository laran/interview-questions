def longest_substring(s: str) -> int:
	"""
	Write a function to return the length of the longest substring in a provided
	string s where all characters in the substring are distinct.
	
	Args:
		s:

	Returns:

	Notes:
		See Also: https://www.hellointerview.com/learn/code/sliding-window/longest-substring-without-repeating-characters

	"""
	state = {}
	start = 0
	max_length = 0
	
	for end in range(len(s)):
		state[s[end]] = state.get(s[end], 0) + 1
		while state[s[end]] > 1:
			state[s[start]] -= 1
			start += 1
			
		max_length = max(max_length, end - start + 1)
	
	return max_length

if __name__ == '__main__':
	assert longest_substring("eghghhgg") == 3
	assert longest_substring("substring") == 8
	