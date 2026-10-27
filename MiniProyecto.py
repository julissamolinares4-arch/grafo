
import heapq


class SistemaGPS:
    def __init__(self):
        
        self.ciudades = {}

    def agregar_ciudad(self, ciudad):
        ciudad = ciudad.strip()

        if not ciudad:
            print("El nombre de la ciudad no puede estar vacío.")
            return

        if ciudad in self.ciudades:
            print("La ciudad ya existe.")
        else:
            self.ciudades[ciudad] = []
            print("Ciudad agregada correctamente.")

    def agregar_ruta(self, origen, destino, minutos):
        origen = origen.strip()
        destino = destino.strip()

        if not origen or not destino:
            print("Los nombres de las ciudades son obligatorios.")
            return

        if origen == destino:
            print("El origen y el destino deben ser diferentes.")
            return

        if minutos < 0:
            print("El tiempo no puede ser negativo.")
            return

        if origen not in self.ciudades:
            self.ciudades[origen] = []

        if destino not in self.ciudades:
            self.ciudades[destino] = []

        
        for vecino, tiempo in self.ciudades[origen]:
            if vecino == destino:
                print("Esta ruta ya existe.")
                return

        
        self.ciudades[origen].append((destino, minutos))
        self.ciudades[destino].append((origen, minutos))

        print("Ruta agregada correctamente.")

    def mostrar_ciudades(self):
        print("\n--- CIUDADES REGISTRADAS ---")

        if not self.ciudades:
            print("Todavía no hay ciudades registradas.")
            return

        for ciudad in sorted(self.ciudades):
            print("-", ciudad)

    def mostrar_rutas(self):
        print("\n--- RUTAS REGISTRADAS ---")

        if not self.ciudades:
            print("No hay rutas registradas.")
            return

        hay_rutas = False

        for origen in sorted(self.ciudades):
            for destino, minutos in self.ciudades[origen]:
                # Mostrar cada carretera una sola vez
                if origen < destino:
                    print(
                        origen, "<->", destino,
                        "| Tiempo:", minutos, "minutos"
                    )
                    hay_rutas = True

        if not hay_rutas:
            print("Todavía no hay carreteras registradas.")

    def dijkstra(self, origen, destino):
        if origen not in self.ciudades:
            return [], None

        if destino not in self.ciudades:
            return [], None

        distancias = {
            ciudad: float("inf")
            for ciudad in self.ciudades
        }

        anteriores = {
            ciudad: None
            for ciudad in self.ciudades
        }

        distancias[origen] = 0
        cola = [(0, origen)]

        while cola:
            tiempo_actual, actual = heapq.heappop(cola)

            if tiempo_actual > distancias[actual]:
                continue

            if actual == destino:
                break

            for vecino, minutos in self.ciudades[actual]:
                nuevo_tiempo = tiempo_actual + minutos

                if nuevo_tiempo < distancias[vecino]:
                    distancias[vecino] = nuevo_tiempo
                    anteriores[vecino] = actual

                    heapq.heappush(
                        cola, (nuevo_tiempo, vecino)
                    )

        if distancias[destino] == float("inf"):
            return [], None

        
        ruta = []
        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.reverse()

        return ruta, distancias[destino]

    def buscar_ruta(self, origen, destino):
        ruta, tiempo = self.dijkstra(origen, destino)

        if tiempo is None:
            print("No existe una ruta entre esas ciudades.")
            return

        print("\n--- RUTA MAS RAPIDA ---")
        print("Origen:", origen)
        print("Destino:", destino)
        print("Recorrido:", " -> ".join(ruta))
        print("Tiempo total:", tiempo, "minutos")


def menu():
    gps = SistemaGPS()

    
    gps.agregar_ruta("Managua", "Masaya", 35)
    gps.agregar_ruta("Managua", "Granada", 50)
    gps.agregar_ruta("Masaya", "Granada", 20)
    gps.agregar_ruta("Granada", "Rivas", 70)
    gps.agregar_ruta("Masaya", "Rivas", 100)

    while True:
        print("\n===== SISTEMA DE NAVEGACION GPS =====")
        print("1. Ver todas las ciudades")
        print("2. Agregar una ciudad")
        print("3. Agregar una ruta")
        print("4. Ver rutas registradas")
        print("5. Buscar la ruta mas rapida")
        print("0. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        try:
            if opcion == "1":
                gps.mostrar_ciudades()

            elif opcion == "2":
                ciudad = input("Nombre de la ciudad: ")
                gps.agregar_ciudad(ciudad)

            elif opcion == "3":
                origen = input("Ciudad de origen: ")
                destino = input("Ciudad de destino: ")

                minutos = float(
                    input("Tiempo del viaje en minutos: ")
                )

                if minutos < 0:
                    print("El tiempo no puede ser negativo.")
                else:
                    gps.agregar_ruta(origen, destino, minutos)

            elif opcion == "4":
                gps.mostrar_rutas()

            elif opcion == "5":
                origen = input("Ciudad de origen: ").strip()
                destino = input("Ciudad de destino: ").strip()

                gps.buscar_ruta(origen, destino)

            elif opcion == "0":
                print("Gracias por utilizar el sistema GPS.")
                break

            else:
                print("Opcion no valida. Intente nuevamente.")

        except ValueError:
            print("Error: debe ingresar un numero valido.")

        except Exception as error:
            print("Ocurrio un error:", error)


if __name__ == "__main__":
    menu()
