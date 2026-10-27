
# Ejercicio 1: Grafo de un arbol genealogico

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_persona(self, persona):
        if persona not in self.adyacencia:
            self.adyacencia[persona] = []

    def agregar_parentesco(self, padre, hijo):
        self.agregar_persona(padre)
        self.agregar_persona(hijo)

        if hijo not in self.adyacencia[padre]:
            self.adyacencia[padre].append(hijo)

    def mostrar_familia(self):
        print("\nARBOL GENEALOGICO")
        print("-------------------------")

        for persona, hijos in self.adyacencia.items():
            print(persona, "->", hijos)



familia = Grafo()


familia.agregar_parentesco("Abuela", "Madre")
familia.agregar_parentesco("Abuela", "Tio")
familia.agregar_parentesco("Madre", "Hija")
familia.agregar_parentesco("Madre", "Hijo")

# Mostrar el resultado
familia.mostrar_familia()
