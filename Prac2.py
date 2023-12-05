# Perform Following tasks
# 1. View data collection forms and import onemode/twomode datasets
# 2. Basic networks

import pandas as pd
import networkx as nx

data_collection_form = pd.DataFrame(
    {
        "Node1": [1, 2, 3, 1, 4],
        "Node2": [2, 3, 4, 5, 5],
        "Weight": [0.5, 0.8, 0.2, 0.7, 0.9],
    }
)

print("\nData Collection Form: ")
print(data_collection_form)

one_mode_data = pd.DataFrame(
    {
        "Node": [1, 2, 3, 4],
        "Attribute1": ["A", "B", "C", "D"],
        "Attribute2": [10, 20, 15, 25],
    }
)

print("\nOneMode Dataset: ")
print(one_mode_data)

two_mode_data = pd.DataFrame(
    {
        "Node1": [1, 2, 3, 1, 4],
        "Node2": ["A", "B", "C", "D", "A"],
        "Weight": [0.5, 0.8, 0.2, 0.7, 0.9],
    }
)

print("\nTwoMode Dataset: ")
print(two_mode_data)

G_one_mode = nx.from_pandas_edgelist(data_collection_form, "Node1", "Node2", ["Weight"])

G_two_mode = nx.from_pandas_edgelist(
    data_collection_form, "Node1", "Node2", ["Weight"], create_using=nx.Graph
)

adj_matrix = nx.to_numpy_array(G_one_mode)
print("\nAdjacency Matrix: ")
print(adj_matrix)
