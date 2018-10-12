import {isEqualTo, isLessThan, exists} from '@laran/readable-helpers';

export default class Staircase {

	/**
	 *
	 * @param numberOfSteps
	 * @param maxStepSize
	 * @param memo a Map, but could also be an array of size numberOfSteps + 1
	 */
	static waysToClimb(numberOfSteps, maxStepSize, memo = {}) {
		if (isLessThan(numberOfSteps, 0)) {
			return 0;
		} else if (isEqualTo(numberOfSteps, 0)) {
			return 1; // This is the most important line. It defines the base-case.
		} else if (exists(memo[numberOfSteps])) {
			return memo[numberOfSteps];
		} else {
			let n = 0;
			for(let i = 1; i <= maxStepSize; i++) {
				n += this.waysToClimb(numberOfSteps - i, maxStepSize, memo);
			}
			memo[numberOfSteps] = n; // set memo atomically
			return n;
		}
	}

}