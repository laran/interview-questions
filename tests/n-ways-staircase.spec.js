import Staircase from "../src/n-ways-staircase";

describe("N-Ways Staircase", () => {

	it('should work with 3 steps and maxStepSize = 3', () => {
		expect(Staircase.waysToClimb(3, 3)).toEqual(4);
		// 1, 1, 1, 1
		// 1, 2
		// 2, 1
		// 3
	});

	it('should work with 3 steps and maxStepSize = 2', () => {
		expect(Staircase.waysToClimb(3, 2)).toEqual(3);
		// 1, 1, 1
		// 1, 2
		// 2, 1
	});

	it('should work with 4 steps and maxStepSize = 2', () => {
		expect(Staircase.waysToClimb(4, 2)).toEqual(5);

		// 1, 1, 1, 1
		// 1, 1, 2
		// 1, 2, 1
		// 2, 1, 1
		// 2, 2
	});
});