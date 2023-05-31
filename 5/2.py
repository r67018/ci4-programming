import random
import timeit


class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.left = None
        self.right = None

    def __str__(self):
        left = f'[{self.left.value}]' if self.left else '[]'
        right = f'[{self.right.value}]' if self.right else '[]'
        return f'{left} <- {self.value} -> {right}'

class BinarySearchTree:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        node = Node(value, len(self.nodes))
        if self.nodes:
            parent, direction = self.find_parent(value)
            if direction == 'left':
                parent.left = node
            else:
                parent.right = node
        self.nodes.append(node)

    def find_parent(self, value):
        node = self.nodes[0]
        while node:
            p = node
            if p.value == value:
                raise ValueError('すでにある値と同じ値を格納することはできません。')
            if p.value > value:
                direction = 'left'
                node = p.left
            else:
                direction = 'right'
                node = p.right
        return p, direction

    def search(self, value):
        root = self.nodes[0]
        return self.__search(root, value)

    def __search(self, node, value):
        if node.value == value:
            return node.index

        if node.value > value:
            return False if node.left is None else self.__search(node.left, value)
        else:
            return False if node.right is None else self.__search(node.right, value)

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return False

size = int(input('size (<= 10000): '))
numbers = random.sample(range(10000), size)
print(numbers)
target = int(input('target: '))

btree = BinarySearchTree()
for v in numbers:
    btree.add_node(v)

t1 = timeit.timeit('linear_search(numbers, target)', globals=globals(), number=1000)
t2 = timeit.timeit('btree.search(target)', globals=globals(), number=1000)
print('linear_search: %.3fs' % (t1))
print('btree.search : %.3fs' % (t2))