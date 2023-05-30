from functools import reduce
from operator import mul

def prime_factorization(a):
    divisors = []
    for i in range(2, a+1):
        while a % i == 0:
            divisors.append(i)
            a //= i
    return divisors


def PrimeFactorization_gcd(a, b):
    factors_a = prime_factorization(a)
    factors_b = prime_factorization(b)
    common = []
    for n in factors_a:
        if n in factors_b:
            common.append(n)
            factors_b.remove(n)

    if len(common) == 0:
        return 1
    return reduce(mul, common)


a = int(input())
b = int(input())
print(PrimeFactorization_gcd(a, b))
