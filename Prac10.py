import networkx as nx


def two_mode_faction_analysis(graph):
    individuals = {
        node
        for node, data in graph.nodes(data=True)
        if data.get("type") == "individual"
    }
    events = {
        node for node, data in graph.nodes(data=True) if data.get("type") == "event"
    }
    bipartite_graph = nx.Graph()
    bipartite_graph.add_nodes_from(individuals, bipartite=0)
    bipartite_graph.add_nodes_from(events, bipartite=1)
    bipartite_graph.add_edges_from(graph.edges())
    individuals_graph = nx.bipartite.projection.projected_graph(
        bipartite_graph, individuals
    )
    factions = list(nx.connected_components(individuals_graph))
    return factions


G = nx.Graph()
G.add_node("Alice", type="individual")
G.add_node("Bob", type="individual")
G.add_node("Party", type="event")
G.add_edge("Alice", "Party")
G.add_edge("Bob", "Party")
result = two_mode_faction_analysis(G)
print("Factions", result)
