# Ejercicio 7:
# Crear un programa que pida al usuario dos números enteros y muestre por pantalla la
# <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números
# introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera
# respectivamente.
'''n = int(input('Ingrese primer número: '))
m = int(input('Ingrese segundo número: '))
c = n // m
r = n % m
print(str(n) + ' entre y ' + str(m) + ' da un cociente ' + str(c) + ' y un resto ' + str(r))'''

def pide_dato(algo):
    dato = input(algo)
    return int(dato)

def cociente(n,m):
    return n // m

def resto(n,m):
    return n % m

def imprime(algo):
	print(algo)

n = pide_dato('Ingrese primer número: ')
m = pide_dato('Ingrese segundo número: ')
imprime((str(n) + ' entre ' + str(m) + ' da un cociente ' + str(cociente(n,m)) + ' y un resto ' + str(resto(n,m))))