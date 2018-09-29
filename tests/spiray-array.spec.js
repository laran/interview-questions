import SpiralArray from "../src/spiral-array";

describe("Spiray Array", () => {

	it("should handle zero", () => {
		expect(SpiralArray.spiralize(0)).toEqual([])
	});

	it("should handle one", () => {
		expect(SpiralArray.spiralize(1)).toEqual([[1]])
	});


	it("should work for even numbers", () => {
		expect(SpiralArray.spiralize(2)).toEqual([
			[1, 2],
			[4, 3]
		])
	});

	it("should work for odd numbers", () => {
		expect(SpiralArray.spiralize(3)).toEqual([
			[1, 2, 3],
			[8, 9, 4],
			[7, 6, 5]
		])
	})
});