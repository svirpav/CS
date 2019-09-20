# import numpy as np
# import sandbox
import kmath
import computer_sciense
import sorting
# import asymptotic as asym
# import plot

''' Class initalization '''
al = computer_sciense.Binary()
srt = computer_sciense.SellectionSort()
insrt = computer_sciense.InsertSearh()
selSrt = sorting.SellectiveSearch()
insSrt = sorting.InsertSearh()
pa = kmath.pAlgebra()

''' Computer sciense part of the code'''

# bin.binary_1()
# bin.binary_2()
# al.binary_3(90, 89)

# array = [7, 9, 4]
# al.swap(array)

# array = [18, 6, 66, 44, 9, 22, 14]
# al.findSmallest(array)

# array = [22, 11, 99, 88, 9, 7, 42, 1, 54, 67, 2, 123, 3, 32, 4, 76, 5]
# srt.sort(array)

# array_2 = [22, 2, 99, 88, 9, 1, 42, 1, 54, 67, 2, -123, 3, 32, 4, 76, 5]
# srt.sort(array_2)

# array = [3, 5, 7, 11, 13, 2, 9, 6]
# insrt.insert(array, 4, 2)
# insrt.insert(array, 5, 9)
# insrt.insert(array, 6, 6)


''' Asymptotic notation '''

# asym.linear(100)
# asym.logorithm(100000)
# asym.polynominal(100)
# [x, y] = asym.logorithmN(100)
# [x1, y1] = asym.polynominal(100)
# plot.quadPlot(y, x)
# plot.dualPlot(x, y, x1, y1)

''' Helpers for Pre-Algebra'''

# palgebra.largest_distributive(56, 32)
# palgebra.logorithm(28)
# palgebra.devisible(262015, 4)
# pa.devisible(13, 4)
# array = np.zeros(325675)
# for i in range(1, len(array)):
#    array[i] = i
# al.bigTehtha(array, 1)
# pa.insertCalculation(5)
# array = [10, -1, -10979]
# pa.arithmeticSum(array)

''' (a1(k) +- a1) '''
# values = [a1, a2]
# pa.sigma(k, n, values)

a1 = -7
a2 = 1
k = 1
n = 625
values = [a1, a2]
[first, last] = pa.sigma(k, n, values)
print(first, last)
pa.findSum(first, last, n)

# [first, last] = pa.findLast(first, step, n)
# print(first, last)
# pa.findSum(first, last, n)

# n = pa.findN(first, second, last)
# pa.findSum(first, last, n)


'''Sandbox : for testing '''
# sandbox.function_1()
# sandbox.loop()
# sandbox.plot()
# sandbox.InsertSearh()
# sandbox.for_range()
''' Sorting examples '''

array = [10, 15, 23, 44, 99, 123, 157, 235, 1, 3, 7, 9, 45, 67, 77, 99, 101,
         505, 33, 21, 17, 19, 59, 323, 289, 103, 19, 0, -1, 2, -9, 59, 1000]
# array = selSrt.sellectiveSearch(array)
# print(array)

# array = insSrt.inserSearch(array)
# print(array)
