
class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append(destino)

    def tiene_ciclo(self):
        visitados = set()
        en_recorrido = set()

        def dfs(vertice):
            visitados.add(vertice)
            en_recorrido.add(vertice)

            for vecino in self.adyacencia[vertice]:
                if vecino not in visitados:
                    if dfs(vecino):
                        return True
                elif vecino in en_recorrido:
                    return True

            en_recorrido.remove(vertice)
            return False

        for vertice in self.adyacencia:
            if vertice not in visitados:
                if dfs(vertice):
                    return True

        return False


# Crear un grafo dirigido
g = Grafo()

# Agregar conexiones que forman un ciclo
g.agregar_arista("A", "B")
g.agregar_arista("B", "C")
g.agregar_arista("C", "A")
g.agregar_arista("C", "D")

# Comprobar si existe un ciclo
if g.tiene_ciclo():
    print("El grafo dirigido contiene un ciclo.")
else:
    print("El grafo dirigido no contiene ciclos.")
