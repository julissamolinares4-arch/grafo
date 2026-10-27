
class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []

        self.adyacencia[origen].append(destino)
        self.adyacencia[destino].append(origen)

    def dfs_iterativo(self, inicio):
        if inicio not in self.adyacencia:
            return []

        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)

                for vecino in reversed(self.adyacencia[actual]):
                    if vecino not in visitados:
                        pila.append(vecino)

        return resultado



g = Grafo()

# Agregar conexiones
g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")
g.agregar_arista("C", "E")


print("Recorrido DFS:", g.dfs_iterativo("A"))
