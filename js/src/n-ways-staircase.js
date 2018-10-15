/**
 *
 * @param numberOfSteps
 * @param maxStepSize
 * @param memo a Map, but could also be an array of size numberOfSteps + 1
 */
export const waysToClimb = (numberOfSteps, maxStepSize, memo = {}) => {
	if (numberOfSteps < 0) {
		return 0;
	} else if (numberOfSteps === 0) {
		return 1; // This is the most important line. It defines the base-case.
	} else if (memo.hasOwnProperty(numberOfSteps)) {
		return memo[numberOfSteps];
	} else {
		let n = 0;
		for (let i = 1; i <= maxStepSize; i++) {
			n += waysToClimb(numberOfSteps - i, maxStepSize, memo);
		}
		memo[numberOfSteps] = n; // set memo atomically
		return n;
	}
};