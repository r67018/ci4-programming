import timeit

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

for i in range(1, 5):
    n = 10 ** i
    print('n = %d: ' % (n))
    a = [random.randint(0, 100) for _ in range(n)]
    t1 = timeit.timeit('sorted(a)', globals=globals(), number=1)
    t2 = timeit.timeit('selection_sort(a)', globals=globals(), number=1)
    print(' sorted: %.10f' % (t1))
    print(' mine  : %.10f' % (t2))
