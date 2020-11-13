# Ejercicio 24:
# Crear un programa que almacene el diccionario con los créditos de las asignaturas de
# un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
# créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
# créditos.  Al final debe mostrar también el número total de créditos del curso.

def carga_dic(curso):
    for i in range(3):
        curso.setdefault(pide_dato('Ingrese asignatura: '), int(pide_dato('Ingrese céditos: ')))

def pide_dato(algo):
    dato = input(algo)
    return dato

def suma_creditos(curso):
    suma = 0
    for i in curso:
        suma = suma + curso.get(i)
    return suma

def imprime(algo):
	print(algo)

def mostrar_dic(curso):
    asignatura = curso.keys()
    credito = curso.values()
    elementos = curso.items()
    for asignatura,credito in elementos:
        imprime(asignatura + ' tiene ' + str(credito) + ' créditos.')

curso = {}
carga_dic(curso)
mostrar_dic(curso)
imprime(suma_creditos(curso))