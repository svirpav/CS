import numpy as np
import random
import math


class Binary:

    def __init__(self):
        print("Class Algorithms initialized")
# My first dirty algorithm :)

    def binary_1(self):
        i_search = 0
        i_last_smallest = 1
        i_cycle = 0
        i_size = 1200
        a = np.zeros(i_size, dtype=int)
        for i in range(0, len(a)):
            a[i] = i+1

        print(a)

        i_number = random.randint(1, len(a))
        print("The number is :", i_number)

        while True:
            i_cycle = i_cycle + 1
            print("Cycle number :", i_cycle)
            i_index = (len(a) / 2) - 1
            i_search = a[i_index]
            print("The new guess number : ", i_search)
            for i in range(0, len(a)):
                if a[i] == i_search:
                    break
            a = np.resize(a, len(a) - (i+1))
            if i_search < i_number:
                print("Too small")
                i_add = i_search + 1
                i_last_smallest = i_search + 1
            if i_search > i_number:
                print("Too big")
                i_add = i_last_smallest
            if i_search == i_number:
                print("The number is : ", i_search)
                break
            for i in range(0, len(a)):
                a[i] = i + i_add
            print(a)
            if len(a) == 1:
                print("Lenght is to short")
                break

    # Second bit better algorithm
    def binary_2(self):
        array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97]
        min = 0
        max = len(array)
        i_cycle = 0

        while(True):
            i_index = ((max - min) / 2) + min
            i_cycle = i_cycle + 1
            if(array[i_index] == 5):
                print("number is found : %d" % array[i_index])
                print("Search cycles %d :" % i_cycle)
                break
            elif(array[i_index] < 5):
                min = i_index
            else:
                max = i_index

    # Optimized uszing math

    def binary_3(self, size, location):
        array = np.zeros(size, dtype=int)
        number = 1
        for i in range(0, size):
            array[i] = number
            number = array[i-1] + array[i]
        min = 0
        max = len(array)
        cycle = 0
        print(len(array))
        while(min < max):
            cycle += 1
            index = int((min + max) / 2)
            if(array[index] == array[location]):
                print("The number is : %d" % array[index])
                print("Search scheck : %d" % array[location])
                break
            elif(array[index] < array[location]):
                min = index + 1
            else:
                max = index - 1
        print("Count cycles : %d" % cycle)

    # Big Tetha anotation

    def bigTehtha(self, array, search):
        for i in range(0, len(array)):
            if(array[i] == search):
                print("Index of search number is : %d " % i)
                break

    # Swaping

    def swap(self, array):
        temp = array[0]
        array[0] = array[1]
        array[1] = temp
        print(array)

    def findSmallest(self, array):
        minValue = array[0]
        minIndex = 0
        for i in range(1, len(array)):
            if(array[i] < minValue):
                minValue = array[i]
                minIndex = i
        print("Min value is %d at index : %d" % (minValue, minIndex))


class SellectionSort:

    @classmethod
    def swap(cls, array, firstIndex, secondIndex):
        temp = array[firstIndex]
        array[firstIndex] = array[secondIndex]
        array[secondIndex] = temp
        return array

    @classmethod
    def findMin(cls, array, startIndex):
        minValue = array[startIndex]
        minIndex = startIndex
        for i in range(startIndex, len(array)):
            if(array[i] < minValue):
                minValue = array[i]
                minIndex = i
        return minIndex

    def sort(self, array):
        for i in range(0, len(array)):
            startIndex = i
            firstIndex = i
            secondIndex = self.findMin(array, startIndex)
            array = self.swap(array, firstIndex, secondIndex)
        print(array)


class InsertSearh:

    def insert(self, array, rightIndex, value):
        key = (len(array) - rightIndex) - 1
        for i in reversed(range(len(array) - key)):
            if(array[i] > value):
                array[i+1] = array[i]
            if(i == 0):
                array[i] = value
            if(array[i] < value):
                array[i+1] = value
                break
        print(array)


class Recursion:

    def method_1(slef, n):
        result = n * math.factorial(n - 1)
        return result

    def rc_factorial(self, n):
        if(n == 0):
            return 1
        return n * self.rc_factorial(n-1)

    def rc_power(self, x, n):
        # base_case
        if(n == 1):
            return 1
        # recursion
        print('call : %d' % n)
        return x * self.rc_power(x, n-1)

    def recursion(self, n):
        if (n > 0):
            print('Call before recusrsion : %d' % n)
            self.recursion(n-1)
            print('call after recusrsion : %d' % n)


class EF_Power:

    def isOdd(self, n):
        return not self.isEven(n)

    def isEven(self, n):
        return ((n % 2) == 0)

    def ef_power(self, x, n):
        # base case
        if(n == 0):
            return 1
        # is isOdd
        elif(n < 0):
            return 1 / self.ef_power(x, abs(n))
        elif(self.isOdd(n)):
            return x * self.ef_power(x, n - 1)
        # is Even
        elif(self.isEven(n)):
            a = self.ef_power(x, n/2)
            return a * a


class Pallindrome:

    def lastCharacter(self, str):
        return str[-1]

    def firstCharacter(self, str):
        return str[0]

    def middleCharacters(self, str):
        return str[1:-1]

    def isPallindrome(self, str):
        # base case nr. 1
        if(len(str) <= 1):
            return True
        # base case nr.2
        elif (self.firstCharacter(str) != self.lastCharacter(str)):
            return False
        return self.isPallindrome(self.middleCharacters(str))


''' Tower of Hanoi '''


class Tower:

    def __init__(self):
        A = [7, 6, 5, 4, 3, 2, 1]
        B = []
        C = []
        self.a = A
        self.b = B
        self.c = C

    def pegToNumber(self, peg):
        if(peg == 'A'):
            a = 0
            return a
        elif(peg == 'B'):
            a = 1
            return a
        elif(peg == 'C'):
            a = 2
            return a

    def numToPeg(self, num):
        if(num == 0):
            return 'A'
        elif(num == 1):
            return 'B'
        elif(num == 2):
            return 'C'

    def getSpare(self, fromPeg, toPeg):
        peg1 = self.pegToNumber(fromPeg)
        peg2 = self.pegToNumber(toPeg)
        a = 3 - peg1 - peg2
        return self.numToPeg(a)

    def moveDisk(self, fromPeg, toPeg):
        if(fromPeg == 'A'):
            if(toPeg == 'B'):
                self.b.append(self.a.pop())
                print(self.a, self.b, self.c)
            else:
                self.c.append(self.a.pop())
                print(self.a, self.b, self.c)
        elif(fromPeg == 'B'):
            if(toPeg == 'A'):
                self.a.append(self.b.pop())
                print(self.a, self.b, self.c)
            else:
                self.c.append(self.b.pop())
                print(self.a, self.b, self.c)
        elif(fromPeg == 'C'):
            if(toPeg == 'A'):
                self.a.append(self.c.pop())
                print(self.a, self.b, self.c)
            else:
                self.b.append(self.c.pop())
                print(self.a, self.b, self.c)

    def solveTower(self, n, fromPeg, toPeg):
        # base_case
        if(n == 0):
            return 1
        # print('Recursion called with : %s -> %s' % (fromPeg, toPeg))
        spare = self.getSpare(fromPeg, toPeg)
        # print('Got Spare %s ' % spare)
        self.solveTower(n - 1, fromPeg, spare)
        self.moveDisk(fromPeg, toPeg)
        self.solveTower(n - 1, spare, toPeg)
