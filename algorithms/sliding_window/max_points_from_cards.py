from typing import List

def max_points_from_cards(cards: List[int], k: int) -> int:
	"""
+
	Given an array of integers representing card values, write a function to
	calculate the maximum score you can achieve by picking exactly k cards.
	
	You must pick cards in order from either end. You can take some cards from
	the beginning, then switch to taking cards from the end, but you cannot skip
	cards or pick from the middle.
	
	For example, with k = 3:
	
	- Take the first 3 cards: valid
	- Take the last 3 cards: valid
	- Take the first card, then the last 2 cards: valid
	- Take the first 2 cards, then the last card: valid
	- Take card at index 0, skip some, then take card at index 5: not valid (skipping cards)

	Args:
		cards:
		k:

	Returns:

	Notes:
		Solution:
			The key insight is to treat the cards excluded from the sum as a
			sliding window. Track the sum of the window, then subtract that sum
			from the total sum of all cards. Iterate through this for all
			windows and the max sum is the result.
		
		See Also:
			- https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards

	"""
	total = sum(cards)
	
	# Handle the special case when k == the number of cards given.
	if k == len(cards):
		return total

	state = 0
	max_points = 0
	start = 0
	
	for end in range(len(cards)):
		state += cards[end]
		
		if end - start + 1 == len(cards) - k:
			max_points = max(total - state, max_points)
			state -= cards[start]
			start += 1

	return max_points

if __name__ == '__main__':
	assert max_points_from_cards([1, 100, 10, 0, 4, 5, 6], 3) == 111
