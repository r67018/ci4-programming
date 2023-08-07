import random
import math

def monte_carlo_integration(f, a, b, samples):
    total = 0
    for _ in range(samples):
        x = random.uniform(a, b)
        total += f(x)
    return (b-a) * total / samples

a = float(input('a: '))
b = float(input('b: '))
samples = int(input('samples: '))

f = lambda x: math.exp(-x)
print(monte_carlo_integration(f, a, b, samples))