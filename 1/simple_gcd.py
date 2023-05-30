def simple_gcd(a, b):
    x = b
    while True:
        if (a % x == 0) and (b % x == 0):
            break
        else:
            x -= 1
    return x

a = int(input())
b = int(input())
print(simple_gcd(a, b))
