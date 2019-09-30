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


class Statistics:

    def permuatation(self, n, k):
        a = math.factorial(n) / math.factorial(n-k)
        b = 1
        for i in range(k):
            c = n - i
            b *= n - i
            print(c)
        print("Version a : %d Version b : %d" % (a, b))

    def plain_factorial(self, a):
        i = math.factorial(a)
        print(i)

    def combinations(self, n, k):
        c = 0
        self.k = math.factorial(k)
        self.p = math.factorial(n-k)
        self.n = math.factorial(n)
        c = self.n / (self.k * self.p)
        print("Amount of combinations in permuatation %d" % c)

    def uniqueComb(self, n, k):
        self.n = math.factorial(n)
        self.k = math.factorial(k)
        print(self.n)
        print(self.k)
        a = self.n / self.k
        print("Unique way : %d" % a)

    def practicalTest(self, n):
        self.n = n - 1
        a = math.factorial(self.n)
        a = a * 2
        print(a)

    def practicalTest_2(self, n, a, b):
        odd = 0
        even = 0
        both = 0
        for i in range(1, n+1):
            if((i % a) == 0):
                even += 1
            if((i % b) == 0):
                odd += 1
            if((i % a) == 0 and (i % b) == 0):
                both += 1
        final = (even + odd) - both
        print("Devisibale by %d = %d" % (a, even))
        print("Devisibale by %d = %d" % (b, odd))
        print("Devisibale by both number %d " % both)
        print("Devisibales %d " % final)

    ''' Probability using combination '''

    def probabilityC(self, tries, options, chance):
        t_outcomes = math.pow(options, tries)
        self.tries = math.factorial(tries)
        self.chance = math.factorial(chance)
        self.comb = math.factorial(tries - chance)
        a = self.tries / (self.chance * self.comb)
        f_prob = (a / t_outcomes) * 100
        # f_prob = round(f_prob, 9)
        print("Probability is %f " % f_prob)
