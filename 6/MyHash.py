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

my_hash_table = HashTable()
my_hash_table.set('taro', 10)
my_hash_table.set('jiro', 20)
print('taro:', my_hash_table.get('taro'))
print('jiro:', my_hash_table.get('jiro'))
