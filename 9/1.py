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

def greedy(items, size_limit):
    sorted_item_list = sorted(items, key=lambda x: x.price/x.weight, reverse=True)
    my_knapsack = Knapsack(size_limit)
    for v in sorted_item_list:
        try:
            my_knapsack.append(v)
        except ValueError:
            continue
    return my_knapsack

# 乱数のシードは章の番号
random.seed(7)

# 品物（Item）は簡単なクラスなのでnamedtupleで作る。
Item = namedtuple('Item', ('name', 'weight', 'price'))

# 品物の個数
num = 20

# 品物を保持するリスト
item_list = []
max_weight = 5
# 品物の個数numより大きな数字にする
max_price = 50

# 値段の候補リストを作り、シャッフル
price_list = list(range(1, max_price+1))
random.shuffle(price_list)

# ランダムに品物を作ってみる。名前は番号
for i in range(num):
    w = random.randint(1, max_weight)
    item = Item(i, w, price_list.pop())
    item_list.append(item)

knap_g = greedy(item_list, 40)
print(knap_g)
