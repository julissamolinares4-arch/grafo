
import heapq

class Red:
    def __init__(self):
        self.conexiones = {}

    def agregar_conexion(self, origen, destino, latencia):
        if origen not in self.conexiones:
            self.conexiones[origen] = []
        if destino not in self.conexiones:
            self.conexiones[destino] = []

        self.conexiones[origen].append((destino, latencia))
        self.conexiones[destino].append((origen, latencia))

    def dijkstra(self, inicio, destino):
        distancias = {
            nodo: float("inf") for nodo in self.conexiones
        }
        distancias[inicio] = 0

        cola = [(0, inicio)]

        while cola:
            latencia_actual, actual = heapq.heappop(cola)

            if latencia_actual > distancias[actual]:
                continue

            if actual == destino:
                return latencia_actual

            for vecino, latencia in self.conexiones[actual]:
                nueva_latencia = latencia_actual + latencia

                if nueva_latencia < distancias[vecino]:
                    distancias[vecino] = nueva_latencia
                    heapq.heappush(
                        cola, (nueva_latencia, vecino)
                    )

        return distancias.get(destino, float("inf"))



red = Red()


red.agregar_conexion("Servidor_A", "Router_1", 10)
red.agregar_conexion("Servidor_A", "Router_2", 20)
red.agregar_conexion("Router_1", "Router_2", 5)
red.agregar_conexion("Router_1", "Servidor_B", 15)
red.agregar_conexion("Router_2", "Servidor_B", 8)


origen = "Servidor_A"
destino = "Servidor_B"

resultado = red.dijkstra(origen, destino)

if resultado == float("inf"):
    print("No existe una ruta entre los servidores.")
else:
    print("Menor latencia:", resultado, "ms")
