import numpy as np
# 7. Crear una matriz de 10x10 con 1 en los bordes y 0 en el interior (con rangos de
# índices).

# 8. Crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4.
array08 = np.random.radint(0, 5, (5, 5))
print (array08)
print('')

# 10. Crear una matriz de 20x20 de valores aleatorios entre 1 y 100, luego indicar su
# media, su mediana, su moda y el desvío estándar. Los valores que den como
# resultado flotantes deben tener como máximo 2 decimales.
array10a = np.random.randint(0, 101, (20,20))
print(array10a)
print('')

# 14. Crear un arreglo de 4 elementos de entre 0 y 10, informar la cantidad de
# elementos que tiene y también cuántos bytes ocupa el arreglo.
array14 = np.random.randint(0, 11, (1,4))
print(array14)


