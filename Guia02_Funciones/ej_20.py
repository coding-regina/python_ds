# Ejercicio 20:
# Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que
# el usuario escriba “salir” que terminará.

def imprime(algo):
    print(algo)

def lee(algo):
    return input(algo)

def cicla():
    entrada = ''
    while entrada != 'salir':
        entrada = lee('Ingrese texto: ')
        imprime(entrada)

cicla()