import random

def selection_sort(_a: list):
    a = _a.copy()
    n = len(a)
    for i in range(n):
        min_j = i
        for j in range(i+1, n):
            if a[j] < a[min_j]:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
    return a

a = [random.randint(0, 100) for _ in range(10)]
print(a)
print(selection_sort(a))
