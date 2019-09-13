import math
import matplotlib.pyplot as plt
import numpy as np


def function_1():
    # Average to int
    index = math.floor((12 + 33) / 2)
    print("Index : %d" % index)
    # Logorith sample
    a = math.log(1580000)
    print("Log : %f" % a)
    # Asymptotic Notation time calculation
    n = 10
    for i in range(0, 10):
        a = 6 * (math.pow(n, 2))
        b = 100 * n + 300
        n += 10
        print("6n^2 : %d VS 300n + 100 : %d" % (a, b))


def loop():
    array = [1, 2, 3, 5, 6, 7]
    for i in reversed(range(len(array) - 3)):
        print(array[i])


def plot():
    n = 10
    y = np.zeros(n)
    x = np.zeros(n)
    y1 = np.zeros(n)
    x1 = np.zeros(n)
    for i in range(1, n):
        y[i] = math.pow(i, 2)
        print("POW of %d = %d " % (i, y[i]))
        x[i] = i
    for i in range(1, n):
        y1[i] = math.exp(i)
        print("EXP of %d = %d " % (i, y1[i]))
        x1[i] = i
    print(math.pow(2, 9))
    plt.plot(x, y, 'r')
    plt.plot(x1, y1, 'b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
