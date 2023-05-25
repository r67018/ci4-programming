import timeit

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return False

array = [1, 2, 3, 4, 5]
targets = [2, 5, 6]
print(f'array: {array}')
for target in targets:
    t1 = timeit.timeit('linear_search(array, target)', globals=globals(), number=1000000)
    t2 = timeit.timeit('target in array', globals=globals(), number=1000000)
    print(f'find {target}: {linear_search(array, target)}')
    print('linear_search: %.3fs' % (t1))
    print('in           : %.3fs' % (t2))