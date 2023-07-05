from collections import namedtuple
import random
import itertools

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

def brute_force(items, size_limit):
    candidate = None
    for pattern in itertools.product((0, 1), repeat=len(items)):
        my_box = []
        for i, val in enumerate(pattern):
            if val:
                my_box.append(item_list[i])
        w = sum([item.weight for item in my_box])
        if w > size_limit:
            continue
        value = sum([item.price for item in my_box])
        if candidate is None or value > candidate.value:
            knapsack = Knapsack(size_limit)
            for v in my_box:
                knapsack.append(v)
            candidate = knapsack
    return candidate

knap_bf = brute_force(item_list, 40)
print(knap_bf)