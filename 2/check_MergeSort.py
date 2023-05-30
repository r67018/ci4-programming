import random
import timeit

def merge_arrays(left, right=[]):
    res = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res + left[i:] + right[j:]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge_arrays(merge_sort(left), merge_sort(right))

random.seed(1)
array = [random.randint(0, 100) for _ in range(500000)]
print(f'n = {len(array)}')
t1 = timeit.timeit('merge_sort(array)', globals=globals(), number=1)
t2 = timeit.timeit('sorted(array)', globals=globals(), number=1)
print('merge_sort: ', t1)
print('sorted    : ', t2)
