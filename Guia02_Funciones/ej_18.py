# Ejercicio 18:
# Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
# una las letras de la palabra introducida empezando por la última.

def pide(algo):
    return input(algo)

def invierte(palabra):
    inversa = palabra[::-1]
    return inversa

def imprime(inversa):
    for i in inversa:
        print(i)

imprime(invierte(pide('Ingrese una palabra: ')))