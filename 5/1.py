def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return False

array = [1, 2, 3, 4, 5]
targets = [2, 5, 6]
print(f'array: {array}')
for target in targets:
    print(f'find {target}: {linear_search(array, target)}')