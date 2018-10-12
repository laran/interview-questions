import {isEqualTo, isLessThan, isLessThanOrEqualTo, isNotEqualTo} from '@laran/readable-helpers'

/**
 * ---
 * Requirements:
 * ---
 *
 * Write a function that determines whether or not two words are exactly "one edit" away.
 *
 * The function should have the following signature:
 *   - bool appliesTo(string s1, string s2)
 *
 *
 * ---
 * Test cases:
 * ---
 *   - appliesTo("cat", "dog") = false
 *   - appliesTo("cat", "cats") = true
 *   - appliesTo("cat", "cut") = true
 *   - appliesTo("cat", "cast") = true
 *   - appliesTo("cat", "at") = true
 *   - appliesTo("cat", "act") = false
 *
 *
 * ---
 * Approach:
 * ---
 * The first thing to do is to figure out what types of edits are allowed.
 *
 * There are two kinds of edit:
 *   - an "insert" (which would require inserting a single character)
 *   - or a "replace" (which would require replacing a single character)
 *
 * A "swap" edit (to handle "cat" and "cta" for example) would require two edits.
 * So it would not be allowed.
 *
 *
 * ---
 * Complexity:
 * ---
 * The complexity for this approach is O(n) as one complete pass through the
 * shortest string is needed.
 */

export default class OneEditAway {

	static _areEqualFrom(a1, i1, a2, i2) {
		// ensure that a1 and a2 have the same number of elements after i1/i2 respectively
		if (isEqualTo(a1.length - i1, a2.length - i2)) {
			while(i1 < a1.length && i2 < a2.length) {
				if (isNotEqualTo(a1[i1], a2[i2])) {
					return false;
				}
				i1++;
				i2++;
			}
			return true;
		}
		return false;
	}

	static _isInsertEdit(a1, i1, a2, i2) {
		return OneEditAway._areEqualFrom(a1, i1, a2, i2 + 1)
			|| OneEditAway._areEqualFrom(a1, i1 + 1, a2, i2);
	}

	static _isReplaceEdit(a1, i1, a2, i2) {
		return OneEditAway._areEqualFrom(a1, i1 + 1, a2, i2 + 1);
	}

	static appliesTo(s1, s2) {

		// s1 and s2 can't be the same string. that would zero edits
		if (isEqualTo(s1, s2)) {
			return false;
		}

		// split each string into a array
		let a1 = s1.split('');
		let a2 = s2.split('');

		let distance = 0;
		let i1 = 0, i2 = 0;
		while (isLessThan(distance, 2) && isLessThan(i1, a1.length) && isLessThan(i2, a2.length)) {
			if (isNotEqualTo(a1[i1], a2[i2])) {
				return OneEditAway._isInsertEdit(a1, i1, a2, i2)
					|| OneEditAway._isReplaceEdit(a1, i1, a2, i2);
			}
			i1++;
			i2++;
		}

		return isLessThanOrEqualTo(distance, 1);
	}
}