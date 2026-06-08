# Sliding Window

A sliding window maintains a contiguous run of elements — a subarray or substring — and slides it across the input,
reusing the work from the previous position instead of recomputing from scratch. It turns the obvious "check every
subarray" O(n·k) or O(n²) brute force into a single O(n) pass. Here are the key things to remember.

**The precondition is contiguity.** A window only works when the answer is a *contiguous* range (a subarray or
substring), not an arbitrary subset. The moment you need to pick elements that aren't adjacent, the window invariant
breaks and you want a different tool (two pointers on a sorted array, a hash map, dynamic programming). If the problem
says "subsequence" rather than "subarray," stop and reconsider.

**There are two main variants.** **Fixed-length** (the window is always exactly `k` wide — add the entering element,
drop the leaving one, evaluate every full window) and **variable-length** (the right edge expands greedily, and the left
edge contracts only when an invariant is violated — used for "longest substring without repeats," "smallest subarray
with sum ≥ target," and similar). Identify which you need before writing code; they have different loop shapes.
`max_subarray_sum` is the fixed-length case.

**The core skill is incremental state: update the window's summary in O(1) as it moves, never rebuild it.** The whole
speedup comes from the fact that sliding by one position changes the window by exactly two elements — one in, one out.
So the running sum, a count, or a frequency map should be *patched*, not recomputed. In `max_subarray_sum`,
`state += nums[end]` adds the entering element and `state -= nums[start]` removes the leaving one; the sum of `k`
elements is maintained without ever re-adding all `k`. If you catch yourself looping over the whole window inside the
outer loop, you've fallen back to O(n·k).

**Know what shrinks the window and when.** In the fixed-length variant the answer is mechanical: the left edge advances
exactly once every time the window reaches width `k`. In the variable-length variant the left edge advances in a `while`
loop, as many times as needed to restore the invariant (no duplicates, sum back under target, etc.). Getting "advance
once" vs. "advance until valid" right is the usual fork in the road.

**Mind the warm-up and the boundaries.** A fixed-length window has a fill phase before the first full window exists —
evaluating too early reads a partial window. The width test `end - start + 1 == k` and the order of "evaluate, then
slide" are the classic bug sites: shrink before you record the answer and you miss the window you just completed.
Initialize the running max to `float('-inf')`, not `0`, so all-negative inputs aren't silently clamped.

**Evaluate at the right moment.** Fixed-length windows are checked once per full window; variable-length windows are
usually checked on every expansion (longest-so-far) or every contraction (smallest-so-far). Decide whether the answer is
read at the top of the loop, after expanding, or after contracting — and do it consistently.

A quick mental test before committing: is the target genuinely contiguous, can I update the window state in O(1) per
step, and do I know exactly when the left edge moves and when I record the answer? If all three hold, the solution is
usually sound.

## When to use a sliding window:

### How to decide to use a fixed-length vs. variable-length sliding window:
- If the problem gives you the window size, use a fixed-length window.
- If the problem gives you a condition and asks for the best-length window meeting it, use a variable-length window.

## Example fixed-length window problems

Use a fixed-length window when the window size `k` is stated in the problem.

1. **Maximum sum of k consecutive elements** — Find the largest sum among all subarrays of length k.
2. **Average of every subarray of size k** — Return the running averages as the window slides.
3. **Maximum of each sliding window of size k** — For each window, report its max (classic deque problem).
4. **First negative number in every window of size k** — Track the first negative as the window advances.
5. **Count anagrams of a pattern in a string** — The window size equals the pattern length; check each window for an 
   anagram match.
6. **Maximum number of vowels in a substring of length k** — Slide a k-length window, count vowels.
7. **Check if any k consecutive elements sum to a target** — Boolean scan over fixed windows.
8. **Number of subarrays of size k with average ≥ threshold** — Count qualifying fixed windows.

## Example variable-length window problems

Use a variable-length window when the window size is discovered by a condition you're optimizing.

1. **Longest substring without repeating characters** — Expand right; contract left when a duplicate appears.
2. **Smallest subarray with sum ≥ target** — Shrink while the sum stays valid, recording the shortest length.
3. **Longest substring with at most k distinct characters** — Contract when distinct count exceeds k. (Here k constrains 
   the content, not the window length.)
4. **Minimum window substring** — Find the shortest substring of s containing all characters of t.
5. **Maximum length subarray with sum equal to target (positive numbers)** — Grow and shrink to hit the exact sum.
6. **Longest subarray with at most k zeros / "max consecutive ones after flipping k zeros"** — Expand until you exceed k 
   flips, then contract.
7. **Fruit into baskets** — Longest subarray containing at most 2 distinct values; same shape as the "at most k distinct" 
   problem.
8. **Subarray product less than k** — Count or size subarrays whose product stays below a bound, contracting when it's 
   exceeded.
9. **Longest repeating character replacement** — Longest window where (window length − count of most frequent char) ≤ k.

## Template for a fixed-length sliding window:

```python
def fixed_length_sliding_window(nums, k):
  state = # choose appropriate data structure
  start = 0
  max_ = 0

  for end in range(len(nums)):
    # extend window
    # add nums[end] to state in O(1) in time

    if end - start + 1 == k: # window is full
      # INVARIANT: size of the window is k here.
      max_ = max(max_, contents of state)

      # contract window
      # remove nums[start] from state in O(1) in time
      
      start += 1 # move left edge to maintain window size of k

  return max_
```

## Template for a variable-length sliding window:

```python
def variable_length_sliding_window(nums):
    state = None      # choose appropriate data structure
    start = 0
    best = 0

    for end in range(len(nums)):
        # extend window: add nums[end] to state in O(1)

        while window_is_invalid(state):
            # contract window: remove nums[start] from state in O(1)
            start += 1

        # INVARIANT: window [start, end] is valid here
        best = max(best, end - start + 1)

    return best
```

## See also

- [Fixed-length sliding window](https://www.hellointerview.com/learn/code/sliding-window/fixed-length)
- [Variable-length sliding window](https://www.hellointerview.com/learn/code/sliding-window/variable-length)
