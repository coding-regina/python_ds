# Ejercicio 12:
# Crear un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede
# dividir por 0.

def nro(msg):
    return float(input(msg))

def imprime(algo):
    print(algo)

def divide():
    nro1 = nro('Ingrese un número: ')
    nro2 = nro('Ingrese otro número: ')
    if nro2 == 0:
        imprime('Error. No se puede dividir por 0.')
    else:
        imprime('La división da ' + str(f"{(nro1/nro2):.2f}")) #redondea a 2 decimales

divide()