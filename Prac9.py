import networkx as nx
import numpy as np
import ast
from networkx.algorithms import bipartite


def two_mode_core_periphery_analysis(graph):
    if not nx.bipartite.is_bipartite(graph):
        raise ValueError("Input graph must be bipartite.")

    nodes_projection = bipartite.projected_graph(graph, graph.nodes())
    adjacency_matrix = nx.to_numpy_array(nodes_projection)
    _, _, Vt = np.linalg.svd(adjacency_matrix)
    threshold = np.median(Vt[0])

    core_nodes = [
        node
        for node, value in zip(nodes_projection.nodes(), Vt[0])
        if value > threshold
    ]

    peripheral_nodes = [
        node
        for node, value in zip(nodes_projection.nodes(), Vt[0])
        if value <= threshold
    ]

    print("Core Nodes:", core_nodes)
    print("Peripheral Nodes:", peripheral_nodes)


if __name__ == "__main__":
    B = nx.Graph()
    B.add_nodes_from([1, 2, 3, 4], bipartite=0)
    B.add_nodes_from(["A", "B", "C"], bipartite=1)
    B.add_edges_from([(1, "A"), (2, "A"), (2, "B"), (3, "B"), (4, "C")])
    two_mode_core_periphery_analysis(B)

