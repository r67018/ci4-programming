def a_k_mod_m(a, k, m):
    b = 1
    for i in reversed(bin(k)[2:]):
        if i == '1':
            b = a * b % m
        a = a**2 % m
    return b

print(a_k_mod_m(7, 43, 123))
print(a_k_mod_m(2, pow(2, 100), 5801))
