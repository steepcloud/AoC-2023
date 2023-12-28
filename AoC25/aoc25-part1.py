import sys
from collections import defaultdict
import networkx as nx

process_input = lambda x: ([[c for c in row] for row in x.strip().split('\n')])

data = open('input.txt').read()
grid = process_input(data)

edges = defaultdict(set)
for line in data.split('\n'):
    source, targets = line.split(':')
    for target in targets.split():
        edges[source].add(target)
        edges[target].add(source)
num_components = len(edges)

graph = nx.DiGraph()
for key, neighbors in edges.items():
    for neighbor in neighbors:
        graph.add_edge(key, neighbor, capacity=1.0)
        graph.add_edge(neighbor, key, capacity=1.0)

for source_node in [list(edges.keys())[0]]:
    for target_node in edges.keys():
        if source_node != target_node:
            cut_value, (left_group, right_group) = nx.minimum_cut(graph, source_node, target_node)
            if cut_value == 3:
                print('Part 1:', len(left_group) * len(right_group))
                break
