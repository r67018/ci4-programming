import random
import timeit
import matplotlib.pyplot as plt

def simple_gcd(a, b):
    x = b
    while True:
        if (a % x == 0) and (b % x == 0):
            break
        else:
            x -= 1
    return x

def euclidean_algorithm(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

REPEAT_COUNT = 200
x = []
simple_gcd_times = []
euclidean_algorithm_times = []
for i in range(REPEAT_COUNT):
    print(i)
    n1 = random.randint(10, 10000000)
    n2 = random.randint(10, 10000000)
    x.append(min(n1, n2))

    t1 = timeit.timeit('simple_gcd(n1, n2)', globals=globals(), number=3)
    t2 = timeit.timeit('euclidean_algorithm(n1, n2)', globals=globals(), number=3)

    simple_gcd_times.append(t1)
    euclidean_algorithm_times.append(t2)

plt.plot(x, simple_gcd_times, '.', label='simple_gcd', markersize=5)
plt.plot(x, euclidean_algorithm_times, '.', label='euclidean_algorithm', markersize=5)
plt.legend()
plt.xlabel('min(a, b)')
plt.ylabel('time')
plt.show()
