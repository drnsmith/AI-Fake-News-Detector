import networkx as nx

def track_misinformation(nodes):
    G = nx.Graph()
    for source, target in nodes:
        G.add_edge(source, target)
    return nx.pagerank(G)
