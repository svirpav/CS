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
    for i in range(len(array)):
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


def InsertSearh():
    array = [33, 5, 19, 34, 1, 62, 7, 45, 99, 22,
             123, 98, 77, 15, 4, 56, 11, 9]
    size = len(array)
    # print(size)
    for index in range(size):
        for i in reversed(range(size - (size - index))):
            if array[i + 1] < array[i]:
                temp = array[i+1]
                array[i + 1] = array[i]
                array[i] = temp
            else:
                break
            print(array)


def for_range():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(1, len(array)):
        print(array[i])


def toInt():
    a = float(1 / 5)
    print(a)


def d2array():
    a = []
    for i in range(5):
        a.append(i)
    b = []
    for i in reversed(range(5)):
        b.append(i)
    c = list(zip(a, b))
    size = len(c[0])
    print(size)


def comapreArray():
    a = [1, 2, 3, 4]
    b = [4, 3, 2, 1]
    c = [1, 2, 3, 4]
    if(a == b):
        print('A = B')
    elif(a == c):
        print('A == C')


def binominal(n, k):
    a = math.factorial(n)
    b = math.factorial(k)
    c = a / b
    print('A = %d, B = %d, C = %d ' % (a, b, c))
    x = math.factorial(n - k)
    y = a / (b * x)
    print('A = %d, B = %d, Y = %d ' % (a, b, y))


def power2(n):
    a = math.pow(2, n)
    print("2^n = %d " % a)


def s_roundup(a, b):
    x = [a, b]
    print(x)
    if(x[0] > x[1]):
        f = math.floor(x[0])
        g = math.ceil(x[1])
    else:
        f = math.ceil(x[0])
        g = math.floor(x[1])
    print('ceil %f : %f' % (a, f))
    print('floor %f : %f ' % (b, g))


def combination(a, b, c):
    n = math.factorial(a)
    k = math.factorial(b)
    n_k = math.factorial(a - b)
    n_1 = math.factorial(c)
    k_1 = math.factorial(a)
    n_1_k = math.factorial(c - a)
    comb = n / (k * n_k)
    all_variations = n_1 / (k_1 * n_1_k)
    print(comb, all_variations)


def birthday(people):
    a = math.pow(365, people)
    b = math.factorial(365)
    c = math.factorial(365 - people)
    d = ((b / c) / a) * 100
    print(d)


def popap():
    a = [1, 2, 3]
    b = []
    # c = []
    b.append(a.pop(0))
    print(a, b)


def findItem():
    a = [1, 2, 3, 4, 5]
    b = []
    print(len(b))
    print(a[len(a)-1])
