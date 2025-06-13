import matplotlib.pyplot as plt # matplotlib.pyplot:para graficar el grafo.
import networkx as nx # networkx: para construir y dibujar gráficos de manera fácil.

# ======= Clases =======
class Edge:
    def __init__(self, u, v, weight): # Crea una arista entre dos nudos uy vcon un peso weight.
        self.u = u
        self.v = v
        self.weight = weight # Una arista une dos nodos uy vcon un peso(coste o beneficio).

    def __repr__(self):
        return f"({self.u}, {self.v}) peso: {self.weight}" # Este método sirve para imprimir el arista de forma clara.

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n)) # Inicializa una lista de padres. Cada nodo empieza siendo su propio padre.
#  Inicializa una lista donde cada nodo es su propio padre.
# Ej: si n = 5, entoncesparent = [0, 1, 2, 3, 4]
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u] # Método find: busca el "líder" del conjunto al que pertenece u. Usa compresión de caminos para acelerar búsquedas futuras.
# Método para encontrar el "jefe" de un conjunto.
# Usa compresión de caminos para que sea más rápido en el futuro.
    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False
    #Une dos conjuntos si no forman un ciclo (si tienen distintos líderes).
    # Devuelve Truesi se unen; False si ya estaban conectados (sería un ciclo).


# ======= Algoritmo Kruskal =======
def kruskal(n, edges, modo="minimo"): 
    # n: número de nodos
    # edges: lista de artistas
    # modo:puede ser "minimo"o"maximo"
    ds = DisjointSet(n)
    mst = []
    total = 0
    # Crea un conjunto disjunto, una lista vacía para el MST y un contador del costo total.

    # Ordena aristas por peso
    sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=(modo == "maximo"))
    # Si es mínimo: de menor a mayor.
    # Si es máximo: de mayor a menor.

    print(f"\nSimulando Árbol de {'Mínimo' if modo == 'minimo' else 'Máximo'} Costo con Kruskal:")
    # Imprima el tipo de árbol que se está generando.
    for edge in sorted_edges: # Recorre todas las aristas ordenadas.
        if ds.union(edge.u, edge.v):
            mst.append(edge)
            total += edge.weight
            print(f"  ✅ Añadido: {edge}") # Si la arista no forma un ciclo, se añade al árbol y se suma su peso.
        else:
            print(f"  ❌ Descartado (ciclo): {edge}") # Si forma un ciclo, se descarta.
    # Recorre cada artista ordenada:
    # Si no forma ciclo, la añade al MST.
    # Si forma ciclo, se descarta.

    print(f"\nCosto total del árbol: {total}")
    print("Aristas del árbol:", mst)
    return mst # Se crea un gráfico de NetworkX con todos los artistas.
    # Al final muestra el costo total del árbol y las aristas que lo componen.

# ======= Visualización Gráfica =======
def graficar_mst(n, edges, mst_edges): #  Función para graficar el árbol generado.
    G = nx.Graph()
    for e in edges:
        G.add_edge(e.u, e.v, weight=e.weight)
    #  Crea un grafo con todas las aristas.

    pos = nx.spring_layout(G, seed=42) # Calcula las posiciones de los nodos automáticamente para que se vean bien.
    edge_labels = {(e.u, e.v): e.weight for e in edges} # Guarda los pesos de cada arista para poner etiquetas en la gráfica.

    plt.figure(figsize=(10, 7)) #  Tamaño de la imagen.
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold') # Se dibujaron en rojo solo los aristas del MST resultante.
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) # Dibuja las etiquetas con los pesos.
    nx.draw_networkx_edges(G, pos, edgelist=[(e.u, e.v) for e in mst_edges], edge_color='red', width=3)
    plt.title("Árbol de Expansión (MST) - Kruskal", fontsize=14)
    plt.axis('off')
    plt.show()

# ======= Datos de Prueba =======
# Estas son las conexiones entre nodos con sus respectivos pesos.
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
# Llama a Kruskal y luego gráfica el árbol generado.
n = 6  # número de nodos
modo = "minimo"  # o "maximo"

mst = kruskal(n, edges, modo=modo)
graficar_mst(n, edges, mst)
