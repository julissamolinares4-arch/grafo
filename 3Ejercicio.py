
from collections import deque

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

    def ruta_mas_corta(self, inicio, destino):
        if inicio not in self.adyacencia or destino not in self.adyacencia:
            return []

        cola = deque([[inicio]])
        visitados = {inicio}

        while cola:
            ruta = cola.popleft()
            actual = ruta[-1]

            if actual == destino:
                return ruta

            for vecino in self.adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(ruta + [vecino])

        return []


g = Grafo()

# Agregar conexiones
g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")
g.agregar_arista("C", "D")
g.agregar_arista("D", "E")


print("Ruta más corta:", g.ruta_mas_corta("A", "E"))
