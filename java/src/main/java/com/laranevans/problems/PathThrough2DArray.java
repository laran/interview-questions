/* (C) Copyright 2017-2018 Laran Evans */
package com.laranevans.problems;

import java.util.*;
import java.util.stream.Collectors;

public class PathThrough2DArray {

	public static void printPath(List<Coordinate> path) {
		if (path == null) {
			System.out.println("No path exists");
			return;
		}
		System.out.println(path.stream()
			.map(Coordinate::toString)
			.collect(Collectors.joining(" -> ")));
	}

	public static List<Coordinate> pathThrough(int[][] matrix) {
		Map<String, Coordinate> coordinates = new HashMap<>();
		for (int y = 0; y < matrix.length; y++) {
			for (int x = 0; x < matrix[y].length; x++) {
				Coordinate coordinate = new Coordinate(x, y);
				coordinate.findNeighbors(matrix);
				coordinates.put(Coordinate.keyFor(coordinate), coordinate);
			}
		}

		List<Coordinate> path = pathBetween(
			coordinates.get(Coordinate.coordsToKey(0, 0)),
			coordinates.get(Coordinate.coordsToKey(matrix[0].length - 1, matrix.length - 1)),
			coordinates);
		return path;
	}

	public static LinkedList<Coordinate> pathBetween(Coordinate origin, Coordinate target, Map<String, Coordinate> coordinates) {
		return pathBetween(origin, target, coordinates, new HashSet<>());
	}

	private static LinkedList<Coordinate> pathBetween(Coordinate origin, Coordinate target, Map<String, Coordinate> coordinates, Set<String> visited) {
		visited.add(origin.key());

		for (String key : origin.getNeighbors()) {
			Coordinate neighbor = coordinates.get(key);
			if (!visited.contains(key)) {
				// base case, we found the target
				if (key.equals(target.key())) {
					LinkedList<Coordinate> path = new LinkedList<>();
					path.add(origin);
					path.add(neighbor);
					// could also just do path.add(target)
					return path;
				} else {
					LinkedList<Coordinate> pathToDestination = pathBetween(neighbor, target, coordinates, visited);
					if (pathToDestination != null) {
						// we found a route
						pathToDestination.addFirst(origin);
						return pathToDestination;
					}
				}
			}
		}

		visited.remove(origin.key());
		return null;
	}

	public static class Coordinate {

		private static int[] DX = new int[]{-1, 0, 1, 0};
		private static int[] DY = new int[]{0, 1, 0, -1};
		int x;
		int y;
		Set<String> neighbors;

		public Coordinate(int x, int y) {
			this.x = x;
			this.y = y;
			this.neighbors = new HashSet<>();
		}

		public static String keyFor(Coordinate coordinate) {
			return coordsToKey(coordinate.x, coordinate.y);
		}

		public static String coordsToKey(int x, int y) {
			return String.format("%s:%s", x, y);
		}

		public static int[] keyToCoords(String key) {
			String[] parts = key.split(":");
			return new int[]{
				Integer.parseInt(parts[0]),
				Integer.parseInt(parts[1])
			};
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

		public void findNeighbors(int[][] matrix) {
			for (int i = 0; i < DX.length; i++) {
				int x1 = this.x + DX[i];
				int y1 = this.y + DY[i];

				if (x1 >= 0 && y1 >= 0) {
					if (y1 < matrix.length) {
						if (x1 < matrix[y1].length) {
							if (matrix[y1][x1] == 0) {
								neighbors.add(coordsToKey(x1, y1));
							}
						}
					}
				}
			}
		}

		@Override
		public String toString() {
			return "(" + x + ", " + y + ")";
		}
	}

}
