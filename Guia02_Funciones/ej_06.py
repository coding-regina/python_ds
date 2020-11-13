# Ejercicio 6:
# Crear un programa que realice la siguiente operación aritmética [(3+2)/2*5]
# 2 . Mostrar el resultado por pantalla.

def calcula():
    return (3+2)/2*5

def imprime(algo):
	print(algo)

imprime('El resultado de la ecuación (3+2)/2*5 es: ' + str(calcula()))
