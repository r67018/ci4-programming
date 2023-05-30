import random
import heapq
import timeit
from typing import List

def merge_sort(array: List[int]):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return heapq.merge(merge_sort(left), merge_sort(right))

array = [random.randint(0, 100) for _ in range(10)]
print(f'n = {len(array)}')
print('before: ', array)
print('after : ', list(merge_sort(array)))
