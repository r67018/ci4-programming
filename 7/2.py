import random
from collections import deque
from matplotlib import pyplot as plt
import networkx as nx

def generate_graph(n, m):
    graph_data = [[0] * n for i in range(n)]
    edge_set = set()
    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j:
            i, j = j, i
        edge_set.add((i, j))
        graph_data[i][j] = graph_data[j][i] = 1
    return graph_data, edge_set

def breath_first_search(start, W):
    work_queue = deque()
    visited = set()

    work_queue.append(start)
    visited.add(start)

    while work_queue:
        here = work_queue.popleft()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_queue.append(i)
                visited.add(i)
    return visited

random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)

print('start from 1:')
print(breath_first_search(1, my_graph))
print('start from 10:')
print(breath_first_search(10, my_graph))

graph = nx.Graph()
graph.add_edges_from(edge_set)
nx.draw_networkx(graph)
plt.show()
