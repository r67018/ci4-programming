import random

def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

a = [random.randint(0, 100) for _ in range(10)]
print(f'{a} -> {is_sorted(a)}')
print(f'{sorted(a)} -> {is_sorted(sorted(a))}')
