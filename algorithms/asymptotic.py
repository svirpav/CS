import numpy as np
import matplotlib.pyplot as plt
import math


def linear(size):
    x = np.zeros(size)
    y = np.zeros(size)
    for i in range(1, size):
        x[i] = i
        y[i] = i
    plt.plot(x, y, 'r')
    plt.title('Linear growth')
    plt.xlabel('Number of Inputs')
    plt.ylabel('Function growth')
    plt.show()


def logorithm(size):
    x = np.zeros(size)
    y = np.zeros(size, dtype=int)
    x1 = np.zeros(size)
    y1 = np.zeros(size, dtype=int)
    x2 = np.zeros(size)
    y2 = np.zeros(size, dtype=int)
    c1 = 2
    c2 = 5
    c3 = 7
    for i in range(1, size):
        x[i] = c1 * math.log(i, 2)
        y[i] = i
        x1[i] = c2 * math.log(i, 2)
        y1[i] = i
        x2[i] = c3 * math.log(i, 2)
        y2[i] = i
    plt.plot(y, x, 'b')
    plt.plot(y1, x1, 'g')
    plt.plot(y2, x2, 'r')
    plt.title('Logorithmig Function Growt')
    plt.xlabel('Number of Inputs')
    plt.ylabel('Function growth')
    plt.show()
