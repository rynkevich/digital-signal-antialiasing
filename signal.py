from math import sin, pi
from random import choice

B1 = 200
B2 = 5
J_MAX = 70
J_INITIAL = 50
N = 512


def test_signal(i):
    eps = lambda: choice((0, 1))
    sin_factor = lambda j=1: sin(2 * pi * i * j / N)
    return B1 * sin_factor() + sum((-1) ** eps() * B2 * sin_factor(j) for j in range(J_INITIAL, J_MAX + 1))
