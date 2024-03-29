# import numpy as np
# import sandbox
import kmath
import computer_sciense
import sorting
import lottery
import complex
# import drawing
# import asymptotic as asym
# import plot

''' Class initalization '''

al = computer_sciense.Binary()
srt = computer_sciense.SellectionSort()
insrt = computer_sciense.InsertSearh()
selSrt = sorting.SellectiveSearch()
insSrt = sorting.InsertSearh()
pa = kmath.pAlgebra()
st = kmath.Statistics()
lot = lottery.Lottery()
rc = computer_sciense.Recursion()
pl = computer_sciense.Pallindrome()
efp = computer_sciense.EF_Power()
tw = computer_sciense.Tower()
dcm = computer_sciense.DivConMe()
qsort = computer_sciense.QuickSort()
cpx = complex.nLogN()

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

# a1 = -7
# a2 = 1
# k = 1
# n = 625
# values = [a1, a2]
# [first, last] = pa.sigma(k, n, values)
# print(first, last)
# pa.findSum(first, last, n)

# [first, last] = pa.findLast(first, step, n)
# print(first, last)
# pa.findSum(first, last, n)

# n = pa.findN(first, second, last)
# pa.findSum(first, last, n)

''' Statistics and probability '''

# st.permuatation(5, 2)
# st.plain_factorial(4)
''' => n! / k!*(n - k)! '''
# st.combinations(8, 3)

# st.uniqueComb(5, 4)
# st.practicalTest(4)
# st.practicalTest_2(100, 10, 7)

# st.probabilityC(30, 2, 3)
# [a, b] = st.coin(4, 2)
# print('Probability is %d/%d' % (a, b))
# st.cpc(5, 10, 6, 4)
# st.fair_coin(5, 3)
# st.sudents(7, 5, 2, 3)


''' Lottery chanches '''

# y = lot.power_ball(69, 5)
# x = [1, 2, 3, 4]
# plot.basicPlot(x, y)
# amount = 60000000
# game = 2
# [games, gpp] = lot.player(amount, game)
# print(games, gpp)

# data = lot.game(5, 69)
# print(data)

'''Sandbox : for testing '''

# sandbox.function_1()
# ssandbox.loop()
# sandbox.plot()
# sandbox.InsertSearh()
# sandbox.for_range()
# sandbox.toInt()
# sandbox.d2array()
# sandbox.comapreArray()
# sandbox.binominal(5, 3)
# sandbox.power2(2)
# sandbox.s_roundup(5.3, 1.8)
# sandbox.combination(5, 3, 69)
# sandbox.birthday(90)
# sandbox.popap()
# sandbox.findItem()
# sandbox.floVSceil()
# sandbox.mulAssign()
# array = [9, 0, 8, 1, 4, 3, 6, 5]
# print(array)
# array = sandbox.workList(array, 0, 0, 1)
# print(array)
# array = sandbox.workList(array, 2, 2, 3)
# print(array)
# array = sandbox.workList(array, 0, 1, 3)
# print(array)
# array = sandbox.workList(array, 4, 4, 5)
# print(array)
# array = sandbox.workList(array, 6, 6, 7)
# print(array)
# array = sandbox.workList(array, 5, 4, 7)
# print(array)
# array = sandbox.workList(array, 0, 3, 7)
# print(array)
# sandbox.quickSort()

''' Sorting examples '''

# array = [10, 15, 23, 44, 99, 123, 157, 235, 1, 3, 7, 9, 45, 67, 77, 99, 101,
#         505, 33, 21, 17, 19, 59, 323, 289, 103, 19, 0, -1, 2, -9, 59, 1000]
# array = selSrt.sellectiveSearch(array)
# print(array)

# array = insSrt.inserSearch(array)
# print(array)

''' Recursive '''

# a = rc.method_1(5)
# print(a)
# a = rc.rc_factorial(25)
# print(a)
# data = pl.isPallindrome('hello')
# print(data)
# data = pl.isPallindrome('a')
# print(data)
# data = pl.isPallindrome('rator')
# print(data)
# a = rc.rc_power(2, 15)
# print(a)
# a = rc.recursion(5)
# print(a)
# print(a)
# a = efp.ef_power(3, 0)
# print(a)
# a = efp.ef_power(3, 1)
# print(a)
# a = efp.ef_power(3, 3)
# print(a)
# a = efp.ef_power(3, -3)
# print(a)
# drawing.drawSquare()


''' Hanoi Tower '''

# tw.solveTower(10, 'A', 'B')


''' Divide Conquer Merge '''

# a = [15, 1, 10, 8, 35, 0, 5, 2]
# x = cpx.complex(len(a))
# print(x)
# a, c = dcm.divideArray(a, 0, len(a)-1)
# print(a, c)

'''     Quick Sort      '''

a = [9, 7, 5, 12, 0, 3, 14, 23, 10, 1, 11, 6]
b = qsort.quickSort(a, 0, len(a) - 1)
print(a, b)
