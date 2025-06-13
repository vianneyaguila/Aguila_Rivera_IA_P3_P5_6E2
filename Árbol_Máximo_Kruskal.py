# Importa las librerías necesarias para graficar el grafo.
import matplotlib.pyplot as plt  # Para mostrar gráficas
import networkx as nx            # Para construir y manejar grafos

# ======= Clases =======

# Clase que representa una arista (conexión entre dos nodos)
class Edge:
    def __init__(self, u, v, weight):
        self.u = u                # Nodo de inicio
        self.v = v                # Nodo de destino
        self.weight = weight      # Peso de la arista (costo o beneficio)

    def __repr__(self):
        return f"({self.u}, {self.v}) peso: {self.weight}"  # Para imprimir la arista de forma legible

# Estructura de conjuntos disjuntos (Union-Find)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Cada nodo comienza siendo su propio padre

    # Método para encontrar el "líder" o raíz del conjunto al que pertenece u
    def find(self, u):
        if self.parent[u] != u:  # Si no es su propio padre, buscar su líder
            self.parent[u] = self.find(self.parent[u])  # Compresión de caminos
        return self.parent[u]

    # Une dos conjuntos si no forman un ciclo
    def union(self, u, v):
        root1 = self.find(u)  # Buscar el líder del conjunto de u
        root2 = self.find(v)  # Buscar el líder del conjunto de v
        if root1 != root2:    # Si pertenecen a conjuntos distintos
            self.parent[root2] = root1  # Unir los conjuntos
            return True       # Se realizó la unión
        return False          # No se unieron (formarían un ciclo)

# ======= Algoritmo de Kruskal =======

# Función que implementa el algoritmo de Kruskal
def kruskal(n, edges, modo="minimo"):
    ds = DisjointSet(n)  # Crear estructura de conjuntos disjuntos
    mst = []             # Lista de aristas del árbol resultante
    total = 0            # Costo total del árbol

    # Ordenar las aristas por peso
    # Si se desea el árbol mínimo: de menor a mayor
    # Si se desea el árbol máximo: de mayor a menor
    sorted_edges = sorted(edges, key=lambda e: e.weight, reverse=(modo == "maximo"))

    print(f"\nSimulando Árbol de {'Mínimo' if modo == 'minimo' else 'Máximo'} Costo con Kruskal:")

    # Recorrer las aristas ordenadas
    for edge in sorted_edges:
        if ds.union(edge.u, edge.v):  # Si no forman un ciclo
            mst.append(edge)          # Añadir arista al árbol
            total += edge.weight      # Sumar su peso al costo total
            print(f"  Añadido: {edge}")
        else:
            print(f"  Descartado (ciclo): {edge}")  # Si forma ciclo, se descarta

    # Mostrar resultados
    print(f"\nCosto total del árbol: {total}")
    print("Aristas del árbol:", mst)
    return mst  # Devolver las aristas del árbol generado

# ======= Visualización Gráfica =======

# Función para graficar el árbol de expansión generado
def graficar_mst(n, edges, mst_edges, modo):
    G = nx.Graph()  # Crear grafo vacío

    # Añadir todas las aristas (originales) al grafo
    for e in edges:
        G.add_edge(e.u, e.v, weight=e.weight)

    # Calcular posiciones para dibujar los nodos
    pos = nx.spring_layout(G, seed=42)

    # Crear etiquetas con los pesos de las aristas
    edge_labels = {(e.u, e.v): e.weight for e in edges}

    # Crear figura para graficar
    plt.figure(figsize=(10, 7))

    # Dibujar nodos y todas las aristas (con etiquetas)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Dibujar en rojo solo las aristas del árbol resultante (MST)
    nx.draw_networkx_edges(G, pos, edgelist=[(e.u, e.v) for e in mst_edges], edge_color='red', width=3)

    # Título de la gráfica según el modo
    tipo = "mínimo" if modo == "minimo" else "máximo"
    plt.title(f"Árbol de Expansión {tipo.capitalize()} (Kruskal)", fontsize=14)

    plt.axis('off')  # Ocultar ejes
    plt.show()       # Mostrar gráfica

# ======= Datos de Prueba =======

# Lista de aristas de prueba: cada una conecta dos nodos y tiene un peso
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

n = 6  # Número de nodos en el grafo

# Puedes cambiar entre "minimo" o "maximo" según lo que quieras generar
modo = "maximo"  # Cambiar a "minimo" si deseas el árbol mínimo

# Ejecutar el algoritmo de Kruskal
mst = kruskal(n, edges, modo=modo)

# Mostrar el grafo con el árbol generado
graficar_mst(n, edges, mst, modo)
