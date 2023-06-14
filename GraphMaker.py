import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def draw_graph_from_adjacency_matrix(adjacency_matrix, node_labels):
    # Tworzenie grafu z macierzy sąsiedztwa
    G = nx.from_numpy_array(adjacency_matrix)

    # Rysowanie grafu
    pos = nx.spring_layout(G, k=2)  # Zwiększenie wartości k zwiększa odległość między węzłami
    nx.draw(G, pos, node_size=800)

    # Dodanie etykiet węzłów
    labels = {i: node_labels[i] for i in range(len(G.nodes))}
    nx.draw_networkx_labels(G, pos, labels, verticalalignment='center')

    # Dodanie etykiet krawędzi
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Wyświetlanie grafu w oknie
    plt.show()


# Definiowanie macierzy sąsiedztwa A o wymiarach 10x10
A = np.array([[0, 4, 0, 0, 0, 0, 0, 2, 0, 0],
              [4, 0, 5, 0, 0, 0, 0, 2, 0, 0],
              [0, 5, 0, 2, 0, 0, 0, 1, 0, 0],
              [0, 0, 2, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 0, 3],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [2, 2, 1, 0, 0, 1, 1, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 3, 0, 0, 0, 0]])

# Definiowanie etykiet węzłów
node_labels = ['rpg', 'dnd', 'bg3', 'dos', 'pre', 'and', 'ios', 'pfr', 'pfk', 'mgg']

# Rysowanie grafu z macierzy sąsiedztwa A
draw_graph_from_adjacency_matrix(A, node_labels)
