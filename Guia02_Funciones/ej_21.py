# Ejercicio 21:
# Crear un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista y muestre por pantalla el
# mensaje “Y o estudio <asignatura>”, donde <asignatura> es cada una de las
# asignaturas de la lista.

def crea_lista():
    lista = ['Matemáticas Discretas', 'Algoritmos', 'Estructuras de Datos', 'Arquitectura de Computadoras', 'Sistemas de Representación']
    return lista

def que_estudio(lista):
    for item in lista:
        print('Yo estudio ' + item)

que_estudio(crea_lista())