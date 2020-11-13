# Ejercicio 11:
# Crear un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable.

def clave(msg):
    return input(msg)

def imprime(algo):
    print(algo)

def check_pass(clave, clave2):
    if clave == clave2:
        imprime('Las contraseñas coinciden.')
    else:
        imprime('Error. Las contraseñas no coinciden.')

check_pass(clave('Ingrese contraseña: '), clave('Reingrese contraseña: '))
