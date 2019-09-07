import numpy as np
import random


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
