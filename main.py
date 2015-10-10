#!/usr/bin/python

import math


def generate_test():
    """
    Make list of points for the RDP code test
    :return: list of points
    """

    # noinspection PyPep8Naming
    R = 5.0

    ptss = []
    for k in range(0, 101):
        x = R - 0.1 * float(k)
        y = -math.sqrt(R * R - x * x)
        ptss.append((x, y))

    for k in range(0, 101):
        x = -R + 0.1 * float(k)
        y = 0.0
        ptss.append((x, y))

    return ptss

if __name__ == "__main__":
    pts = generate_test()

    for pt in pts:
        print(pt)
