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

def bb(items, size_limit):
    knapsack = Knapsack(size_limit)
    cand = knapsack
    def _bb(knapsack, items):
        if len(items) == 0:
            if knapsack.value > cand.value:
                cand = knapsack
            return
        else:
            # don't take
            knap1 = _bb(knapsack, items[1:])
            knap2 = knapsack
            # take
            if knapsack.has_room_for(items[0]):
                next_knapsack = Knapsack(knapsack.size)
                for v in knapsack.items:
                    next_knapsack.append(v)
                next_knapsack.append(items[0])
                knap2 = _bb(next_knapsack, items[1:])
            if knap1.value > knap2.value:
                return knap1
            else:
                return knap2

    return _bb(knapsack, items)

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