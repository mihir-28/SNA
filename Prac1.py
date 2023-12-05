# Write a program to compute for the following
# 1. Number of Edges
# 2. Number of Nodes
# 3. Degree of Node
# 4. Node with lowest Degree
# 5. The adjacency list
# 6. Matrix of the graph

import networkx as nx
import numpy as np


def compute_graph_properties(graph):
    num_edges = graph.number_of_edges()
    num_nodes = graph.number_of_nodes()
    node_degrees = dict(graph.degree())
    min_degree = min(node_degrees, key=node_degrees.get)
    adjacency_list = dict(graph.adjacency())
    adjacency_matrix = nx.adjacency_matrix(graph).todense()

    return (
        num_edges,
        num_nodes,
        node_degrees,
        min_degree,
        adjacency_list,
        adjacency_matrix,
    )


G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

edges, nodes, degrees, min_degree, adj_list, adj_matrix = compute_graph_properties(G)

print("Number of Edges: ", edges)
print("Number of Nodes: ", nodes)
print("Degree of each node: ", degrees)
print("Node with lowest degree: ", min_degree)
print("Adjacency List: ", adj_list)
print("Adjacency Matrix: \n", adj_matrix)