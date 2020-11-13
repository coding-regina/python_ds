# Ejercicio 13:
# Crear un programa que pida al usuario un número entero y muestre por pantalla si es
# par o impar .

def pide_num():
    return int(input('Ingrese un número entero: '))

def imprime(algo):
    print(algo)

def analize(num):
    if num%2 == 0:
        imprime('El número es par')
    else:
        imprime('El número es impar')

analize(pide_num())