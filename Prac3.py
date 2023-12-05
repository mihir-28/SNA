# Compute the following node level measures
# 1. Density
# 2. Degree
# 3. Reciprocity
# 4. Transitivity
# 5. Centralization
# 6. Clustering

import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

density = nx.density(G)
print(f"Density: {density}")

degree = dict(G.degree())
print(f"Degree: {degree}")

reciprocity = nx.reciprocity(G)
print(f"Reciprocity: {reciprocity}")

transitivity = nx.transitivity(G)
print(f"Transitivity: {transitivity}")

centralization = nx.degree_centrality(G)
print(f"Centralization: {centralization}")

clustering = nx.clustering(G)
print(f"Clustering: {clustering}")
