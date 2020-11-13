# Ejercicio 17:
# Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def calcula():
    for i in range(10):
        print('\nTABLA DEL ',(i+1),'\n==============')
        for j in range(10):
            print((j+1), ' x' ,(i+1),' = ',((j+1)*(i+1)))

calcula()