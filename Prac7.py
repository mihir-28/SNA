import networkx as nx
import matplotlib.pyplot as plt

persons = ["Person1", "Person2", "Person3", "Person4"]
committees = ["CommitteeA", "CommitteeB", "CommitteeC"]

G = nx.Graph()
G.add_nodes_from(persons, bipartite=0)
G.add_nodes_from(committees, bipartite=1)

G.add_edges_from(
    [
        ("Person1", "CommitteeA"),
        ("Person1", "CommitteeB"),
        ("Person2", "CommitteeB"),
        ("Person3", "CommitteeC"),
        ("Person4", "CommitteeA"),
    ]
)

pos = nx.bipartite_layout(G, persons)
nx.draw(
    G,
    pos,
    with_labels=True,
    font_weight="bold",
    node_color="skyblue",
    font_color="black",
    node_size=800,
)
plt.title("Persons_by-Committees Bipartite Graph")
plt.show()

persons_graph = nx.bipartite.projected_graph(G, persons)
pos_persons = nx.spring_layout(persons_graph)
nx.draw(
    persons_graph,
    pos_persons,
    with_labels=True,
    font_weight="bold",
    node_color="lightgreen",
    font_color="black",
    node_size=800,
)
plt.title("Persons-by-Person Network")
plt.show()

committees_graph = nx.bipartite.projected_graph(G, committees)
pos_committees = nx.spring_layout(committees_graph)
nx.draw(
    committees_graph,
    pos_committees,
    with_labels=True,
    font_weight="bold",
    node_color="lightcoral",
    font_color="black",
    node_size=800,
)
plt.title("Committees-by-Committees Network")
plt.show()
