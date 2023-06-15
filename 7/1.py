import random
import networkx as nx
import matplotlib.pyplot as plt

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
print(edge_set)

graph = nx.Graph()
for u, v in edge_set:
    graph.add_edge(u, v)
nx.draw_networkx(graph)
plt.show()
