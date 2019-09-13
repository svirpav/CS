import numpy as np
import random


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
