import math
import random
import heapq

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

def dijkstra(start, W):
    distance_list = [math.inf] * len(W)
    distance_list[start] = 0
    done_list = []
    wait_heap = []
    for i, d in enumerate(distance_list):
        heapq.heappush(wait_heap, (d, i))

    while wait_heap:
        p = heapq.heappop(wait_heap)
        i = p[1]
        if i in done_list:
            continue
        done_list.append(i)

        for j, x in enumerate(W[i]):
            if x == 1 and j not in done_list:
                d = min(distance_list[j], distance_list[i] + x)
                distance_list[j] = d
                heapq.heappush(wait_heap, (d, j))
    return distance_list

random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
print(dijkstra(10, my_graph))