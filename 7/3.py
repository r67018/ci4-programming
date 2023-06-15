import random
import networkx as nx
import matplotlib.pyplot as plt

def depth_first_search(start, W):
    work_stack = []
    visited = set()
    work_stack.append(start)
    visited.add(start)

    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_stack.append(i)
                visited.add(i)
    return visited

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

random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)

print('start from 10:')
print(depth_first_search(10, my_graph))

graph = nx.Graph()
graph.add_edges_from(edge_set)
nx.draw_networkx(graph)
plt.show()
