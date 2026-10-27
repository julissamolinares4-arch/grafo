
import heapq

class GrafoPonderado:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, costo):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []

        self.adyacencia[origen].append((destino, costo))
        self.adyacencia[destino].append((origen, costo))

    def dijkstra(self, inicio):
        distancias = {
            ciudad: float("inf")
            for ciudad in self.adyacencia
        }
        distancias[inicio] = 0
        cola = [(0, inicio)]

        while cola:
            costo_actual, ciudad = heapq.heappop(cola)

            if costo_actual > distancias[ciudad]:
                continue

            for vecino, costo in self.adyacencia[ciudad]:
                nuevo_costo = costo_actual + costo

                if nuevo_costo < distancias[vecino]:
                    distancias[vecino] = nuevo_costo
                    heapq.heappush(
                        cola, (nuevo_costo, vecino)
                    )

        return distancias

    def mostrar(self):
        for ciudad, vuelos in self.adyacencia.items():
            print(ciudad, "->", vuelos)



vuelos = GrafoPonderado()


vuelos.agregar_arista("Managua", "Panama", 200)
vuelos.agregar_arista("Managua", "San Jose", 120)
vuelos.agregar_arista("San Jose", "Panama", 50)
vuelos.agregar_arista("Panama", "Madrid", 500)
vuelos.agregar_arista("San Jose", "Madrid", 700)


print("SISTEMA DE VUELOS")
vuelos.mostrar()


print("\nCostos minimos desde Managua:")
distancias = vuelos.dijkstra("Managua")

for ciudad, costo in distancias.items():
    print(ciudad, ":", costo)
