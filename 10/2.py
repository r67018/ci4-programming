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

def bt(items, size_limit):
    knapsack = Knapsack(size_limit)
    best_knap = knapsack
    def _bt(knapsack, items):
        nonlocal best_knap
        if len(items) == 0:
            if knapsack.value > best_knap.value:
                best_knap = knapsack
            return
        else:
            # don't take
            _bt(knapsack, items[1:])
            # take
            next_knapsack = Knapsack(knapsack.size)
            for v in knapsack.items:
                next_knapsack.append(v)
            try:
                next_knapsack.append(items[0])
                _bt(next_knapsack, items[1:])
            except ValueError:
                if knapsack.value > best_knap.value:
                    best_knap = knapsack
                return

    _bt(knapsack, items)
    return best_knap

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

knapsack = bt(item_list, 40)
print(knapsack)