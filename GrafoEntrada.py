
class GrafoDirigido:
    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].append(destino)

    def calcular_grados(self):
        grados_entrada = {
            vertice: 0 for vertice in self.adyacencia
        }
        grados_salida = {}

        for origen, destinos in self.adyacencia.items():
            grados_salida[origen] = len(destinos)

            for destino in destinos:
                grados_entrada[destino] += 1

        print("Grados de los nodos:")
        for vertice in self.adyacencia:
            print(
                vertice,
                "- Entrada:", grados_entrada[vertice],
                "- Salida:", grados_salida[vertice]
            )

g = GrafoDirigido()


g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "C")
g.agregar_arista("C", "D")
g.agregar_arista("D", "A")


g.calcular_grados()
