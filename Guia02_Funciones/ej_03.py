# Ejercicio 3:
# Crear un programa que pida al usuario nombre y edad e imprima dichos datos en
# renglones distintos.

def imprime(algo):
	print(algo)

def pideDatos():
	nombre = input('Ingrese su nombre: ')
	imprime('Su nombre es ' + nombre)
	edad = input('Ingrese su edad: ')
	imprime('Su edad es ' + str(edad) + ' años')

pideDatos()