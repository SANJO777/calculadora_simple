from decimal import *

class CalculadoraSimple:

    def __init__(self, nombre_calculadora):
        self.nombre_calculadora = nombre_calculadora

    # Menú en consola. Asimismo, retorna al menú principal al imprimir el resultado de la operación hecha.
    def menú(self):
        pass

    # Valida números racionales, operadores y expresiones simples ingresados para operar, en vez de letras o carácteres inválidos.
    def validar_números(self):
        pass

    # Operación Aritmética: Adición.
    def sumar(self):
        pass

    # Operación Aritmética: Substracción.
    def resta(self):
        pass

    # Operación Aritmética: Multiplicación.
    def multiplicación(self):
        pass

    # Operación Aritmética: División.
    def división(self):
        pass

    # Operación Aritmética: Porcentaje.
    def porcentaje(self):
        pass

calculadora_simple = CalculadoraSimple("Kuromi")
print(calculadora_simple.nombre_calculadora)
