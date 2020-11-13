# Ejercicio 10:
# Crear un programa que pida al usuario su edad y muestra por pantalla si es mayor de
# edad o no, siendo 18 años la mayoría de edad.

def pide_dato(msg):
    return int(input(msg))

def procesa(dato):
    if dato >= 18:
        imprime('Tiene ' + str(dato) + ' años. Es mayor de edad.')
    else:
        imprime('Tiene ' + str(dato) + ' años. Es menor de edad.')

def imprime(algo):
    print(algo)

procesa(pide_dato('Ingrese su edad: '))