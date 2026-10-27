
from dataclasses import dataclass, field
from collections import deque


@dataclass
class GrafoDirigido:
    # Cada nodo apunta a una lista de sus vecinos salientes.
    adyacencia: dict[str, list[str]] = field(default_factory=dict)

    def agregar_nodo(self, nombre: str) -> None:
        """Agrega un nodo si todavía no existe."""
        if nombre not in self.adyacencia:
            self.adyacencia[nombre] = []

    def agregar_arista(self, origen: str, destino: str) -> None:
        """Agrega una conexión dirigida: origen -> destino."""
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)

    def buscar_nodo(self, nombre: str) -> bool:
        """Indica si el nodo existe."""
        return nombre in self.adyacencia

    def buscar_arista(self, origen: str, destino: str) -> bool:
        """Indica si existe la conexión dirigida origen -> destino."""
        return destino in self.adyacencia.get(origen, [])

    def obtener_vecinos(self, nombre: str) -> list[str]:
        """Devuelve una copia de los vecinos salientes del nodo."""
        return list(self.adyacencia.get(nombre, []))

    def dfs(self, inicio: str) -> list[str]:
        """Recorre los nodos alcanzables usando búsqueda en profundidad."""
        if inicio not in self.adyacencia:
            return []

        visitados = set()
        orden = []
        pila = [inicio]

        while pila:
            actual = pila.pop()

            if actual in visitados:
                continue

            visitados.add(actual)
            orden.append(actual)

            pila.extend(reversed(self.adyacencia[actual]))

        return orden

    def bfs(self, inicio: str) -> list[str]:
        """Recorre los nodos alcanzables usando búsqueda en anchura."""
        if inicio not in self.adyacencia:
            return []

        visitados = {inicio}
        orden = []
        cola = deque([inicio])

        while cola:
            actual = cola.popleft()
            orden.append(actual)

            for vecino in self.adyacencia[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return orden

    def eliminar_arista(self, origen: str, destino: str) -> None:
        """Elimina la conexión dirigida origen -> destino, si existe."""
        if destino in self.adyacencia.get(origen, []):
            self.adyacencia[origen].remove(destino)

    def eliminar_nodo(self, nombre: str) -> None:
        """Elimina el nodo y las conexiones que llegan a él."""
        if nombre not in self.adyacencia:
            return

        del self.adyacencia[nombre]

        for vecinos in self.adyacencia.values():
            if nombre in vecinos:
                vecinos.remove(nombre)

    def actualizar_nombre_nodo(
        self,
        nombre_actual: str,
        nombre_nuevo: str
    ) -> bool:
        """Cambia el nombre de un nodo y actualiza sus conexiones."""
        if nombre_actual not in self.adyacencia:
            return False

        if nombre_nuevo in self.adyacencia:
            return False

        vecinos_salientes = self.adyacencia.pop(nombre_actual)
        self.adyacencia[nombre_nuevo] = vecinos_salientes

        for vecinos in self.adyacencia.values():
            for indice, vecino in enumerate(vecinos):
                if vecino == nombre_actual:
                    vecinos[indice] = nombre_nuevo

        return True


def mostrar_grafo(grafo):
    print("\nGrafo dirigido:")
    if not grafo.adyacencia:
        print("El grafo está vacío.")
    else:
        for nodo, vecinos in grafo.adyacencia.items():
            print(nodo, "->", vecinos)


def menu():
    grafo = GrafoDirigido()

    while True:
        print("\n===== MENÚ DE GRAFO DIRIGIDO =====")
        print("1. Agregar nodo")
        print("2. Agregar arista")
        print("3. Buscar nodo")
        print("4. Buscar arista")
        print("5. Consultar vecinos")
        print("6. Recorrido DFS")
        print("7. Recorrido BFS")
        print("8. Eliminar arista")
        print("9. Eliminar nodo")
        print("10. Actualizar nombre de nodo")
        print("11. Mostrar grafo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del nodo: ")
            if grafo.buscar_nodo(nombre):
                print("El nodo ya existe.")
            else:
                grafo.agregar_nodo(nombre)
                print("Nodo agregado correctamente.")

        elif opcion == "2":
            origen = input("Ingrese el nodo de origen: ")
            destino = input("Ingrese el nodo de destino: ")
            if grafo.buscar_arista(origen, destino):
                print("La arista ya existe.")
            else:
                grafo.agregar_arista(origen, destino)
                print("Arista agregada correctamente.")

        elif opcion == "3":
            nombre = input("Ingrese el nodo que desea buscar: ")
            if grafo.buscar_nodo(nombre):
                print("El nodo existe.")
            else:
                print("El nodo no existe.")

        elif opcion == "4":
            origen = input("Ingrese el nodo de origen: ")
            destino = input("Ingrese el nodo de destino: ")
            if grafo.buscar_arista(origen, destino):
                print("La arista existe.")
            else:
                print("La arista no existe.")

        elif opcion == "5":
            nombre = input("Ingrese el nodo: ")
            if grafo.buscar_nodo(nombre):
                print("Vecinos:", grafo.obtener_vecinos(nombre))
            else:
                print("El nodo no existe.")

        elif opcion == "6":
            inicio = input("Ingrese el nodo inicial para DFS: ")
            print("Recorrido DFS:", grafo.dfs(inicio))

        elif opcion == "7":
            inicio = input("Ingrese el nodo inicial para BFS: ")
            print("Recorrido BFS:", grafo.bfs(inicio))

        elif opcion == "8":
            origen = input("Ingrese el nodo de origen: ")
            destino = input("Ingrese el nodo de destino: ")
            if grafo.buscar_arista(origen, destino):
                grafo.eliminar_arista(origen, destino)
                print("Arista eliminada correctamente.")
            else:
                print("La arista no existe.")

        elif opcion == "9":
            nombre = input("Ingrese el nodo que desea eliminar: ")
            if grafo.buscar_nodo(nombre):
                grafo.eliminar_nodo(nombre)
                print("Nodo eliminado correctamente.")
            else:
                print("El nodo no existe.")

        elif opcion == "10":
            actual = input("Ingrese el nombre actual del nodo: ")
            nuevo = input("Ingrese el nuevo nombre: ")
            if grafo.actualizar_nombre_nodo(actual, nuevo):
                print("Nombre actualizado correctamente.")
            else:
                print("No se pudo actualizar. Verifique los nombres.")

        elif opcion == "11":
            mostrar_grafo(grafo)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
