import networkx as nx
import numpy as np
from scipy.linalg import svd


def svd_analysis(graph):
    adjacency_matrix = nx.to_numpy_array(graph)
    U, S, Vt = svd(adjacency_matrix)
    print("U matrix:")
    print(U)
    print("\nSingular values:")
    print(S)
    print("\nV transpose matrix:")
    print(Vt)


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 5), (1, 3), (2, 3), (2, 5)])
    svd_analysis(G)
