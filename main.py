from decimal import *

class CalculadoraSimple:

    # Constructor con atributo de instancia (no de clase) de prueba. 
    def __init__(self, nombre_calculadora):
        self.nombre_calculadora = nombre_calculadora

    # Otra clase o sub-clase menú en consola. Asimismo, retorna al menú principal al imprimir el resultado de la operación hecha.
        
        # 1. Mostrar menú: suma, resta, multiplicación, división y porcentaje.
        # 2. Escoger una operación aritmética.
        # 3. Digitar los números para hacer la operación.
        # 4. Resultado.
        # 5. Regresar al menú 1.
        # ¿Cómo puedo mezclar diferentes operaciones aritméticas en consola?
        # -> Supuestamente escribiendo la expresión completa y respetando orden: primero resolver * y /, luego + y - (sin paréntesis).
        # Escribir un parse o algo para que respete jerarquías de las calculadoras simples.
    
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

    # Operación Aritmética: Porcentaje, «fórmula de internet para obtener porcentajes sin paréntesis en mi calculadora simple».
    def porcentaje(self):
        pass

calculadora_simple = CalculadoraSimple("Kuromi")
print(calculadora_simple.nombre_calculadora)
