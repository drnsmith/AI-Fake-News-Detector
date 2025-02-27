import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_fake_news_graph(articles):
    """
    Builds a graph to analyze how misinformation spreads.
    Each article is a node, and connections represent shared sources or reposts.
    """
    G = nx.DiGraph()

    # Add nodes (articles)
    for i, article in enumerate(articles):
        G.add_node(i, title=article["title"])

    # Randomly link articles to simulate propagation
    for i in range(len(articles)):
        for j in range(i + 1, len(articles)):
            if random.random() < 0.3:  # 30% chance of link
                G.add_edge(i, j)

    return G

def visualize_graph(G):
    """
    Displays the misinformation spread network.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="red", font_size=10)
    plt.title("Misinformation Spread Graph")
    plt.show()

# Example Usage (for testing)
if __name__ == "__main__":
    sample_articles = [
        {"title": "Fake News 1"},
        {"title": "Fake News 2"},
        {"title": "Legit News"},
        {"title": "Viral Fake Story"},
    ]
    G = generate_fake_news_graph(sample_articles)
    visualize_graph(G)

