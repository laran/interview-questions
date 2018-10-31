// To generate the array call SpiralArray.spiralize(n)
// To print the array call SpiralArray.print(SpiralArray.spiralize(n))
export default class SpiralArray {

	// Walk around the box at a given depth
	static fill(i, a, xmin, xmax, ymin, ymax) {
		// fill top row
		let x = xmin;
		let y = ymin;
		for(; x < xmax; x++) {
			a[ymin][x] = i++;
		}
		// fill right column
		for(; y < ymax; y++) {
			a[y][xmax] = i++;
		}
		// fill bottom row
		for(; x > xmin; x--) {
			a[ymax][x] = i++;
		}
		// fill left column
		for(; y > ymin; y--) {
			a[y][xmin] = i++;
		}
	}

	static spiralize(n) {

		// initialize storage
		let a = [];
		for(let i = 0; i < n; i++) {
			a[i] = new Array(n);
		}

		// fill the storage array walking in from the outside
		for(let i = 0; i < n/2; i++) {
			SpiralArray.fill(
				i * n + 1,
				a,
				i,
				n-i-1,
				i,
				n-i-1
			);
		}

		// fill in the center spot when n is odd
		if (n % 2 === 1) {
			a[(n-1)/2][(n-1)/2] = n*n;
		}

		return a;
	}

	// print a 2d matrix
	static print(a2d) {
		console.log(a2d.map((row) => { return row.join(', '); }).join('\n'));
	}
}