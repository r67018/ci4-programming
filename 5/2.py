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

        res_left = self.__search(node.left, value) if node.left else False
        res_right = self.__search(node.right, value) if node.right else False
        if res_left:
            return res_left
        elif res_right:
            return res_right
        else:
            return False

btree = BinarySearchTree()
for v in [10, 20, 12, 4, 3, 9, 30]:
    btree.add_node(v)

print(btree.search(30))