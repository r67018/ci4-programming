def euclidean_algorithm(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r

a = int(input())
b = int(input())
print(euclidean_algorithm(a, b))
