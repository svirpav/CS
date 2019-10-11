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

    ''' Coins probability '''

    def coin(self, flips, heads):
        i_min = 0
        i_pos = math.pow(2, flips)
        x = math.factorial(flips)
        y = math.factorial(flips - heads)
        z = math.factorial(heads)
        combination = x/(y * z)
        for i in range(1, int(combination+1)):
            if((combination % i) == 0 and (i_pos % i) == 0):
                i_min = i
        combination = combination / i_min
        i_pos = i_pos / i_min
        return combination, i_pos

    def fair_coin(slef, flips, tails):
        a = math.pow(2, flips)
        b = math.factorial(flips)
        c = math.factorial(tails)
        d = math.factorial(flips - tails)
        e = b / (c * d)
        f = e / a
        print(f)

    def sudents(self, stud, by, gy, grp):
        a = math.factorial(stud)
        b = math.factorial(grp)
        c = math.factorial(stud - grp)
        d = a / (b * c)
        print(d)
        x = math.factorial(by)
        y = math.factorial(by - grp)
        z = x / (b * y)
        print(z)
        print(z/d)

    ''' Conditional Probability and Compbination '''
    def cpc(self, fair, unfair, n, k):
        sum = fair + unfair
        pr_a = fair / sum
        pr_b = unfair / sum
        print("Prob A : %f " % pr_a)
        print('Prob B : %f ' % pr_b)
        fpb = \
            (math.factorial(n) / (math.factorial(k)
             * math.factorial(n-k))) / math.pow(2, n)
        print('Fair coinf probab 4/6 : %f' % fpb)
        ufpb = \
            (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))\
            * (math.pow(0.8, 4) * math.pow(0.2, 2))
        print('unfair probability 4/6 : %f' % ufpb)
        x = pr_a * fpb + pr_b * ufpb
        print('Total probability getting 4/6 : %f' % x)
        y = (fpb * pr_a) / x
        print('Probabili to have 4(failr)/6 : %f' % y)
