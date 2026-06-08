def longest_repeating_characters(s: str, k: int) -> int:
	"""
	Write a function to find the length of the longest substring containing the
	same letter in a given string s, after performing at most k operations in
	which you can choose any character of the string and change it to any other
	uppercase English letter.
	
	The question is asking:

	Given a string like "BBABCCDD" and a number k, what is the longest
	contiguous chunk you can make into all the same letter if you’re allowed to
	change at most k characters?
	
	Args:
		s:
		k:

	Returns:

	"""
	
	# Counts characters inside the current sliding window.
	# Example window "AABBB" -> {"A": 2, "B": 3}
	state = {}
	
	# The highest frequency of any single character we've seen in the window.
	# This tells us which character we would keep if we made the window uniform.
	max_freq = 0
	
	# Best valid window length found so far.
	max_length = 0
	
	# Left edge of the sliding window.
	start = 0
	
	# end is the right edge of the sliding window.
	for end in range(len(s)):
		# Add the new character on the right side of the window.
		state[s[end]] = state.get(s[end], 0) + 1
		
		# Update the count of the most common character.
		max_freq = max(max_freq, state[s[end]])
		
		# Current window length is end - start + 1.
		#
		# To make the whole window one repeated character, we would keep the
		# most frequent character and replace all the others.
		#
		# replacements_needed = window_length - max_freq
		#
		# This condition is the same as:
		# window_length - max_freq > k
		#
		# Meaning: this window needs too many replacements, so shrink it.
		if k + max_freq < end - start + 1:
			# Remove the leftmost character from the window.
			state[s[start]] -= 1
			
			# Move the left edge right by one.
			start += 1
		
		# Record the largest valid window length seen so far.
		max_length = max(max_length, end - start + 1)
	
	return max_length


if __name__ == '__main__':
	assert longest_repeating_characters("BBABCCDD", 2) == 5