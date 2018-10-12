/* (C) Copyright 2017-2018 Laran Evans */
package com.laranevans.questions;

import java.util.*;
import java.util.stream.Collectors;

public class PathThrough2DArray {

	// A set of moves to make to check for neighbors in all directions
	private static int[] DX = new int[]{-1, 0, 1, 0};
	private static int[] DY = new int[]{0, 1, 0, -1};

	/**
	 * Display the path if one exists.
	 *
	 * @param path
	 */
	public static void printPath(List<Coordinate> path) {
		if (path == null) {
			System.out.println("No path exists");
			return;
		}
		System.out.println(path.stream()
			.map(Coordinate::toString)
			.collect(Collectors.joining(" -> ")));
	}

	/**
	 * Find a path through the matrix.
	 *
	 * @param matrix
	 * @return
	 */
	public static List<Coordinate> pathThrough(int[][] matrix) {
		Map<String, Coordinate> coordinates = new HashMap<>();
		for (int y = 0; y < matrix.length; y++) {
			for (int x = 0; x < matrix[y].length; x++) {
				Coordinate coordinate = new Coordinate(x, y);
				findNeighbors(coordinate, matrix);
				coordinates.put(Coordinate.keyFor(coordinate), coordinate);
			}
		}

		List<Coordinate> path = pathBetween(
			coordinates.get(Coordinate.coordsToKey(0, 0)),
			coordinates.get(Coordinate.coordsToKey(
				matrix[0].length - 1, matrix.length - 1)),
			coordinates);
		return path;
	}

	private static LinkedList<Coordinate> pathBetween(
		Coordinate origin, Coordinate target, Map<String, Coordinate> coordinates) {
		return pathBetween(origin, target, coordinates, new HashSet<>());
	}

	private static LinkedList<Coordinate> pathBetween(
		Coordinate origin, Coordinate target, Map<String, Coordinate> coordinates,
		Set<String> visited) {

		// Remember what coordinate we're at to avoid cycles in our path.
		visited.add(origin.key());

		for (String key : origin.getNeighbors()) {
			Coordinate neighbor = coordinates.get(key);
			if (!visited.contains(key)) {
				// base case, we found the target
				if (key.equals(target.key())) {
					LinkedList<Coordinate> path = new LinkedList<>();
					path.add(origin);
					path.add(neighbor);
					return path;
				} else {
					LinkedList<Coordinate> pathToDestination =
						pathBetween(neighbor, target, coordinates, visited);
					if (pathToDestination != null) {
						// We found a route. Prepend origin to the route and pass it
						// back up the call stack all the way back to the top left
						// coordinate.
						pathToDestination.addFirst(origin);
						return pathToDestination;
					}
				}
			}
		}

		// We're leaving origin without finding a path.
		// Remove origin from the set of visited coordinates to allow
		// other coordinates to pass through origin to look for a path.
		visited.remove(origin.key());

		return null;
	}

	// Check which paths adjacent to a Coordinate are passable.
	private static void findNeighbors(Coordinate coordinate, int[][] matrix) {
		for (int i = 0; i < DX.length; i++) {
			int x1 = coordinate.x + DX[i];
			int y1 = coordinate.y + DY[i];

			if (x1 >= 0 && y1 >= 0) {
				if (y1 < matrix.length) {
					if (x1 < matrix[y1].length) {
						if (matrix[y1][x1] == 0) {
							coordinate.neighbors.add(Coordinate.coordsToKey(x1, y1));
						}
					}
				}
			}
		}
	}

	/**
	 * Represents an x,y coordinate and reachable neighbors.
	 */
	public static class Coordinate {

		private int x;
		private int y;
		private Set<String> neighbors;

		public Coordinate(int x, int y) {
			this.x = x;
			this.y = y;
			this.neighbors = new TreeSet<>();
		}

		public static String keyFor(Coordinate coordinate) {
			return coordsToKey(coordinate.x, coordinate.y);
		}

		public static String coordsToKey(int x, int y) {
			return String.format("%s:%s", y, x);
		}

		public int getX() {
			return x;
		}

		public int getY() {
			return y;
		}

		public String key() {
			return keyFor(this);
		}

		public Set<String> getNeighbors() {
			return neighbors;
		}

		public void setNeighbors(Set<String> neighbors) {
			this.neighbors = neighbors;
		}

		@Override
		public String toString() {
			return "(" + y + ", " + x + ")";
		}
	}

}
