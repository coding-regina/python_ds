# Ejercicio 22:
# Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre
# por pantalla su producto escalar .

def crea_lista(x,y,z):
    lista = [x,y,z]
    return lista

def imprime(algo):
    print(algo)

def prod_escalar(vector1, vector2):
    prod_esc = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    imprime('El producto escalar entre ' + str(vector1) + ' y ' + str(vector2) + ' es ' + str(prod_esc))

prod_escalar(crea_lista(1,2,3), crea_lista(-1,0,2))