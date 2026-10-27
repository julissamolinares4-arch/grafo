
import heapq

class GrafoPonderado:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, peso):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []

        self.adyacencia[origen].append((destino, peso))
        self.adyacencia[destino].append((origen, peso))

    def dijkstra(self, inicio, destino):
        distancias = {
            nodo: float("inf") for nodo in self.adyacencia
        }
        anteriores = {nodo: None for nodo in self.adyacencia}

        if inicio not in self.adyacencia or destino not in self.adyacencia:
            return [], float("inf")

        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            distancia_actual, actual = heapq.heappop(cola)

            if distancia_actual > distancias[actual]:
                continue

            if actual == destino:
                break

            for vecino, peso in self.adyacencia[actual]:
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = actual
                    heapq.heappush(cola, (nueva_distancia, vecino))

        if distancias[destino] == float("inf"):
            return [], float("inf")

        ruta = []
        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.reverse()
        return ruta, distancias[destino]



g = GrafoPonderado()


g.agregar_arista("A", "B", 4)
g.agregar_arista("A", "C", 2)
g.agregar_arista("C", "B", 1)
g.agregar_arista("B", "D", 5)
g.agregar_arista("C", "D", 8)


ruta, costo = g.dijkstra("A", "D")

if ruta:
    print("Ruta más corta:", " -> ".join(ruta))
    print("Costo mínimo:", costo)
else:
    print("No existe una ruta entre los nodos.")
