# For a given network find the following
# 1. Length of the shortest path from a given node to another node
# 2. The density of the graph
# 3. Draw egocentric network of node G with chosen configuration parameters

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 5), (1, 3), (2, 3), (2, 5), (3, 4), (4, 5)])

shortest_path_length = nx.shortest_path_length(G, source=1, target=5)
print(f"Shortest Path length from Node1 to Node5: {shortest_path_length}")

density = nx.density(G)
print(f"Graph Density: {density}")

ego_node = 2
egocentric_network = nx.ego_graph(G, ego_node, radius=1)
pos = nx.spring_layout(egocentric_network)

nx.draw(
    egocentric_network,
    pos,
    with_labels=True,
    node_color="pink",
    node_size=300,
    font_size=10,
    font_color="black",
)
plt.title(f"Egocentric Network of Node {ego_node}")
plt.show()
