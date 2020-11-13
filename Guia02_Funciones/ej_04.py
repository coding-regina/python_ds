# Ejercicio 4:
# Crear un programa que pregunte el nombre del usuario y un número entero e imprima
# por pantalla en líneas distintas el nombre del usuario tantas veces como el número
# introducido.

def imprime(algo, veces):
    for i in range(veces):
        print(algo)

repeticiones = pideDato('Cuántas repeticiones? ')
imprime(nombre, int(repeticiones))