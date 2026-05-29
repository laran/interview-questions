# Two Pointers

The two-pointer technique uses two indices moving through a data structure to avoid the nested-loop brute force, typically trading O(n²) for O(n). Here are the key things to remember.

**The precondition is usually order.** Most two-pointer solutions require the data to be sorted (or have some monotonic property). The whole reason a pointer can move "confidently" in one direction is that order guarantees what lies beyond it. If the input isn't sorted and order matters, sorting first (O(n log n)) is often still worth it. Your triangle_number is exactly this: the sort is what licenses counting right - left in bulk.

**There are two main variants.** **Opposite-ends** (pointers start at both ends and converge — used for sorted-sum, container-with-most-water, palindrome checks) and **same-direction** (both start at the front, one races ahead — used for sliding windows, removing duplicates in place, fast/slow cycle detection). Identify which you need before writing code; they have different invariants.

**The core skill is the invariant: at each step, know why moving a pointer cannot skip a valid answer.** In opposite-ends sum problems, if a + b is too large you move the right pointer in because every element left of it is smaller and would only make the sum smaller still — so no answer is lost. Being able to state that sentence is the difference between a correct solution and one that silently misses cases. If you can't articulate why a move is safe, the algorithm is probably wrong.

**Each pointer should move monotonically.** The efficiency comes from each pointer traversing the array at most once, giving O(n). If you find yourself resetting a pointer backward inside the loop, you've likely collapsed back into O(n²) and should reconsider.

**Mind the boundary conditions.** The loop guard (left < right vs left <= right), where pointers start, and when you stop are the usual bug sources. Off-by-one errors here are extremely common — your loop's range(..., 1, -1) stopping point and the left < right guard are precisely the spots that need a comment, which is why you annotated them.

**Counting vs. collecting.** A subtle but powerful move: when order is established, a single found match can imply a whole batch (as in count += right - left). Watch for opportunities to count in bulk rather than enumerate one at a time — it's often what separates an accepted solution from a time-limit-exceeded one.

A quick mental test before committing: can I name the invariant, confirm each pointer moves one way only, and verify the boundary? If all three hold, the solution is usually sound.

## Examples

| File | Problem |
| --- | --- |
| [`two_sum.py`](two_sum.py) | Two Sum (sorted input) |
| [`container_with_most_water.py`](container_with_most_water.py) | Container With Most Water |
| [`three_sum.py`](three_sum.py) | 3Sum |
| [`triangle_number.py`](triangle_number.py) | Valid Triangle Number |
| [`move_zeroes.py`](move_zeroes.py) | Move Zeroes |
| [`sort_colors.py`](sort_colors.py) | Sort Colors (Dutch national flag) |

[`array_utils.py`](array_utils.py) holds the shared `swap` helper used by the in-place examples.

Each example file is self-contained and runnable, with its inline assertions guarded under `if __name__ == "__main__":`. Run one directly from this directory, e.g.:

```bash
python move_zeroes.py
```
