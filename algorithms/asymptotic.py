import numpy as np
import math


def linear(size):
    x = np.zeros(size, dtype=int)
    y = np.zeros(size, dtype=int)
    for i in range(1, size):
        x[i] = i
        y[i] = i
    return [x, y]


def logorithm(size):
    y = np.zeros(size)
    x = np.zeros(size, dtype=int)
    for i in range(1, size):
        y[i] = math.log(i, 2)
        x[i] = i
    return [x, y]


def polynominal(size):
    x = np.zeros(size, dtype=int)
    y = np.zeros(size)
    for i in range(1, size):
        y[i] = math.pow(i, 2)
        x[i] = i
    return [x, y]


def logorithmN(size):
    x = np.zeros(size, dtype=int)
    y = np.zeros(size)
    for i in range(1, size):
        y[i] = (i * math.log(i, 2))
        x[i] = i
    return [x, y]
