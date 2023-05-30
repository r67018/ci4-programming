import random
import time
import sys

sys.setrecursionlimit(2500)

def quick_sort(array):
    if array == []:
        return array
    p = array[-1]
    left = []
    right = []
    pivots = []
    for v in array:
        if v < p:
            left.append(v)
        elif v > p:
            right.append(v)
        else:
            pivots.append(v)
    return quick_sort(left) + pivots + quick_sort(right)

def quick_sort2(array):
    if not array:
        return array
    pivot = random.choice(array)
    left = []
    right = []
    pivots = []
    for v in array:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            pivots.append(v)
    return quick_sort(left) + pivots + quick_sort(right)

def performance_check(method, data, num=3):
    s = time.time()
    for _ in range(num):
        for v in data:
            method(v)
    e = time.time()
    return e - s

random.seed(1)
sample_data = []
for _ in range(100):
    sample_data.append(sorted([random.randint(0, 5000) for _ in range(2000)]))
t1 = performance_check(quick_sort, sample_data)
t2 = performance_check(quick_sort2, sample_data)
print('quick_sort 4.5: ', t1)
print('quick_sort 4.7: ', t2)