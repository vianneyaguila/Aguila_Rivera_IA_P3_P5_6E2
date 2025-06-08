import matplotlib.pyplot as plt
import networkx as nx

# ======= Clases =======
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __repr__(self):
        return f"({self.u}, {self.v}) peso: {self.weight}"

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False

# ======= Algoritmo Kruskal =======
def kruskal(n, edges, modo="minimo"):
    ds = DisjointSet(n)
    mst = []
    total = 0

    # Ordena aristas por peso
    sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=(modo == "maximo"))

    print(f"\nSimulando Árbol de {'Mínimo' if modo == 'minimo' else 'Máximo'} Costo con Kruskal:")
    for edge in sorted_edges:
        if ds.union(edge.u, edge.v):
            mst.append(edge)
            total += edge.weight
            print(f"  ✅ Añadido: {edge}")
        else:
            print(f"  ❌ Descartado (ciclo): {edge}")

    print(f"\nCosto total del árbol: {total}")
    print("Aristas del árbol:", mst)
    return mst

# ======= Visualización Gráfica =======
def graficar_mst(n, edges, mst_edges):
    G = nx.Graph()
    for e in edges:
        G.add_edge(e.u, e.v, weight=e.weight)

    pos = nx.spring_layout(G, seed=42)
    edge_labels = {(e.u, e.v): e.weight for e in edges}

    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_edges(G, pos, edgelist=[(e.u, e.v) for e in mst_edges], edge_color='red', width=3)
    plt.title("Árbol de Expansión (MST) - Kruskal", fontsize=14)
    plt.axis('off')
    plt.show()

# ======= Datos de Prueba =======
edges = [
    Edge(0, 1, 4),
    Edge(0, 2, 3),
    Edge(1, 2, 1),
    Edge(1, 3, 2),
    Edge(2, 3, 4),
    Edge(3, 4, 2),
    Edge(4, 5, 6)
]

# ======= Ejecución =======
n = 6  # número de nodos
modo = "minimo"  # o "maximo"

mst = kruskal(n, edges, modo=modo)
graficar_mst(n, edges, mst)
