# Ejercicio 16:
# Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los
# años que ha cumplido (desde 1 hasta su edad).

def edad(msg):
    return int(input('Ingrese su edad: '))

def imprime(algo):
    print(algo)

def bucle(edad):
    for i in range(edad):
        imprime(i + 1)

bucle(edad('Ingrese su edad: '))