import math


class pAlgebra:

    def __init__(self):
        print("Pre-Agebra is initialized")

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
