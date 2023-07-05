from collections import namedtuple
import random


class Knapsack:
    def __init__(self, size):
        self.size = size
        self.weight = 0
        self.value = 0
        self.items = []

    def append(self, item):
        if not self.has_room_for(item):
            raise ValueError('このアイテムは入れられません。重量オーバーです。')
        self.items.append(item)
        self.weight += item.weight
        self.value += item.price

    def has_room_for(self, item):
        return self.size >= self.weight + item.weight

    def __str__(self):
        return '重さ {}kg / 価値 {}万円\nアイテム {}'.format(self.weight, self.value, self.items)

def dp(items, size_limit):
    n = len(items)
    table = [[0] * (size_limit+1) for i in range(n+1)]
    flag = [[False] * (size_limit+1) for i in range(n+1)]

    for i in range(1, n+1):
        target = items[i-1]
        w = target.weight
        for j in range(1, size_limit+1):
            yellow = table[i-1][j]
            table[i][j] = yellow
            if w > j:
                continue
            pink = table[i-1][j-w]
            include_this = target.price + pink
            table[i][j] = max(yellow, include_this)
            flag[i][j] = include_this > yellow
    i = n
    j = size_limit
    my_knapsack = Knapsack(size_limit)
    while i > 0 and j > 0:
        if flag[i][j]:
            my_knapsack.append(items[i-1])
            j -= items[i-1].weight
        i -= 1
    return my_knapsack

random.seed(7)

Item = namedtuple('Item', ('name', 'weight', 'price'))

num = 20

item_list = []
max_weight = 5
max_price = 50

price_list = list(range(1, max_price+1))
random.shuffle(price_list)

for i in range(num):
    w = random.randint(1, max_weight)
    item = Item(i, w, price_list.pop())
    item_list.append(item)

knap_dp = dp(item_list, 40)
print(knap_dp)
