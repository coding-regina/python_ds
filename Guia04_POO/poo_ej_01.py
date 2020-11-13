# Ejercicio 1
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construir los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● mostrar(): Muestra los datos de la persona.
# ● esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.__dni = dni

    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad}. Su nro de DNI es {self.__dni}")

    def esMayorDeEdad(self):
        retorno = False
        if self.edad >= 18:
            retorno = True
        return retorno

jose = Persona('José', 39, 33456345)
mariana = Persona('Mariana', 16, 40345339)

jose.mostrar()
print(jose.esMayorDeEdad())
mariana.mostrar()
print(mariana.esMayorDeEdad())