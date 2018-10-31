import OneEditAway from "../src/one-edit-away";

describe("One Edit Away", () => {
	it("should pass all sample tests", () => {
		expect(OneEditAway.appliesTo("cat", "dog")).toBe(false);
		expect(OneEditAway.appliesTo("cat", "cats")).toBe(true);
		expect(OneEditAway.appliesTo("cat", "cut")).toBe(true);
		expect(OneEditAway.appliesTo("cat", "at")).toBe(true);
		expect(OneEditAway.appliesTo("cat", "act")).toBe(false);
		expect(OneEditAway.appliesTo("cat", "cast")).toBe(true);
	})
});