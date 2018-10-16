/**
 *
 * @param numberOfSteps
 * @param maxStepSize
 */
export const waysToClimb = (numberOfSteps, maxStepSize) => {
	// initialize base cases
	let memo = {0: 1, 1: 1};

	// we already know the answer when steps < 2. so solve for steps > 1
	for (let currentStep = 2; currentStep <= numberOfSteps; currentStep++) {
		memo[currentStep] = 0;

		// accumulate the sum of combinations for all step sizes from 1 to min(currentStep, maxStepSize)
		for (let stepSize = 1; stepSize <= currentStep && stepSize <= maxStepSize; stepSize++) {
			memo[currentStep] = memo[currentStep] + memo[currentStep - stepSize];
		}
	}

	return memo[numberOfSteps];
};