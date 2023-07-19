import random
import sys
import timeit

def f(n):
    a = [random.random() for _ in range(n)]
    print(f'used memory: {sys.getsizeof(a)} bytes')

n = random.randint(1, 50000000)
print(f'n = {n}')
t = timeit.timeit('f(n)', globals=globals(), number=1)
print('time: {:.3f} seconds'.format(t))
