import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido vacío
G = nx.DiGraph()

# Añadimos nodos al grafo dirigido
G.add_nodes_from([1, 2, 3, 4])

# Añadimos arcos (conexiones dirigidas) entre nodos y etiquetas
edges = [(1, 2, {'label': 'A'}), (1, 3, {'label': 'B'}), (2, 3, {'label': 'C'}), (3, 4, {'label': 'D'})]
G.add_edges_from(edges)

# Dibujamos el grafo dirigido con etiquetas en las flechas
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', arrows=True)

# Añadimos las etiquetas de las flechas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostramos el grafo dirigido
plt.show()
