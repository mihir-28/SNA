# Write a program to distinguish between
# 1. A network as a matrix
# 2. A network as an edge list,
# 3. A network as a sociogram (or “network graph”)
# 4. Using 3 distinct networks representatives of each


import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 5), (1, 3), (2, 3), (2, 5), (3, 4), (4, 5)])

matrix_representation = nx.to_numpy_array(G)
print("Network as a matrix: ")
print(matrix_representation)

edge_list_representation = nx.to_edgelist(G)
print("\nNetwork as an edge list: ")
print(edge_list_representation)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight="bold")
plt.title("Network as a sociogram")
plt.show()
