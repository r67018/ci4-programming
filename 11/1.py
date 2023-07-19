def prime_test(n):
    m = int(pow(n, 0.5))
    for d in range(2, m + 1):
        if n % d == 0:
            return False
    return True

print(71, prime_test(71))
print(5489, prime_test(5489))
