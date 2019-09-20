import math


class pAlgebra:

    def largest_distributive(a, b):
        if(a < b):
            for i in range(1, a+1):
                c = a % i
                d = b % i
                if(c == 0 and d == 0):
                    print("%d modulo of (%d) :(%d) and (%d) : (%d)"
                          % (i, a, c, b, d))
        else:
            for i in range(1, b+1):
                c = a % i
                d = b % i
                if(c == 0 and d == 0):
                    print("%d modulo of (%d) :(%d) and (%d) : (%d)"
                          % (i, a, c, b, d))

    def logorithm(z):
        c = math.sqrt(z)
        print("Log^2 a : %f " % c)

    def devisible(self, a, b):
        c = a % b
        print("Modulo : %d" % c)

    def insertCalculation(slef, k):
        x = 0
        for i in range(1, k+1):
            x += i
            print(i)
        print(x)
        y = (1 + k) * k/2.0
        print(y)

    ''' Arythmetic Sum '''

    def arithmeticSum(slef, array):
        d = array[1] - array[0]
        n = array[2] - array[0]
        n = n / d
        n = n + 1
        print("d = %f" % n)
        sn = ((array[0] + array[2]) / 2.0) * n
        print("Sum(n) : %d" % sn)

    def sigma(slef, k, n, values):
        f = []
        for i in range(k, 3):
            f.append((values[0] * i) + values[1])
        d = f[1] - f[0]
        aLast = f[0] + (n-1)*d
        first = f[0]
        return first, aLast

    def findLast(slef, first, d, n):
        aLast = first + ((n-1)*d)
        print(aLast)
        return first, aLast

    def findSum(self, first, last, n):
        aSum = (first + last) / 2.0
        print('(first + last) / 2 %f ' % aSum)
        aSum = aSum * n
        print('aSum : %d ' % aSum)

    def findN(self, first, second, last):
        d = second - first
        print(d)
        n = (last - first) / d
        n += 1
        print(n)
        return n
