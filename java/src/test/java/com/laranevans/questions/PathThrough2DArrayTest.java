/* (C) Copyright 2017-2018 Laran Evans */
package com.laranevans.questions;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

@DisplayName("PathThrough2DArray")
public class PathThrough2DArrayTest {

	@Test
	public void shouldFindAPath() {
		int[][] matrix = new int[][] {
			{0, 0, 0, 0, 0, 0, 0},
			{0, 0, 1, 0, 0, 1, 0},
			{0, 0, 1, 0, 1, 1, 0},
			{0, 0, 1, 0, 1, 0, 1},
			{1, 1, 1, 0, 0, 0, 0}
		};
		List<PathThrough2DArray.Coordinate> path = PathThrough2DArray.pathThrough(matrix);
		PathThrough2DArray.printPath(path);

		assertThat(path, is(notNullValue()));
		assertThat(path.size(), is(greaterThan(0)));
	}
}
