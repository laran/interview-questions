"""
Usage:
    spiralize(n)

Example:
    This code:

        print_spiral(spiralize(3))

    Produces this output:

        1, 2, 3
        8, 9, 4
        7, 6, 5
"""


def spiralize(n):
    """
    Create a 2-dimensional list of ints with numbers increasing in a
    clockwise spiral starting from the top left corner ([0][0])

    :param n:
    :return:
    """
    if n == 0:
        return []

    # fully initialize the matrix
    a = [] * n
    for i in range(n):
        a.append([0] * n)

    for i in range(int(n / 2)):
        fill(i * n + 1, a, i, n - i - 1, i, n - i - 1)

    if n % 2 == 1:
        a[int((n - 1) / 2)][int((n - 1) / 2)] = int(n * n)

    return a


def fill(i, a, xmin, xmax, ymin, ymax):
    """
    Walk all the way around the matrix at a given depth

    :param i:
    :param a:
    :param xmin:
    :param xmax:
    :param ymin:
    :param ymax:
    :return:
    """
    for x in range(xmax):
        a[ymin][x] = i
        i += 1

    for y in range(ymax):
        a[y][xmax] = i
        i += 1

    for x in range(xmax, 0, -1):
        a[ymax][x] = i
        i += 1

    for y in range(ymax, 0, -1):
        a[y][xmin] = i
        i += 1


def print_spiral(a2d):
    """
    Print a 2-dimensional array of integers

    :param a2d:
    :return:
    """
    print('')  # newline for clarity
    for y in range(len(a2d)):
        row = a2d[y]
        print(", ".join(str(x) for x in row))
