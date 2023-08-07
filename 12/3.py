def fermat_check(n):
    cnt = 0
    for a in range(2, n):
        if pow(a, n-1, n) != 1:
            cnt += 1
    return cnt

print(71, fermat_check(71))
print(99, fermat_check(99))
print(1105, fermat_check(1105))
