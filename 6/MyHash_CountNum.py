import random

class HashTable:
    def __init__(self, table_size=100):
        self.data = [[] for i in range(table_size)]
        self.n = table_size

    def get_hash(self, v):
        return hash(v) % self.n

    def search(self, key):
        i = self.get_hash(key)
        for j, v in enumerate(self.data[i]):
            if v[0] == key:
                return (i, j)
        return (i, -1)

    def set(self, key, value):
        i, j = self.search(key)
        if j != -1:
            self.data[i][j][1] = value
        else:
            self.data[i].append([key, value])

    def get(self, key):
        i, j = self.search(key)
        if j != -1:
            return self.data[i][j][1]
        raise KeyError(f'{key} was not found in this HashTable!')

hash_table = HashTable()
for _ in range(300):
    key = random.randint(0, 1000)
    value = random.randint(0, 1000)
    hash_table.set(key, value)

print('hash: num of data')
for i in range(100):
    print(f'{i}: {len(hash_table.data[i])}')