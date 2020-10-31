# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import numpy as np
from scipy import stats

lista_numeros = [100, 9, -5, -5, 6, 99, 200, 44, 21, 789, -10, -11, 21, 30]
print('Lista  : ', lista_numeros)

arr_numeros = np.array(lista_numeros)
print('Arreglo: ', arr_numeros)

media = np.mean(arr_numeros)
print('Media: ', media)

mediana = np.median(arr_numeros)
print('Mediana: ', mediana)

cuartil = np.percentile(arr_numeros, 25)
print('Percentiles: ', cuartil)

moda = stats.mode(arr_numeros)
print('Moda: ', moda)

varianza = np.var(arr_numeros)
print(f"Varianza: {varianza:.2f}")

desvio_e = np.std(arr_numeros)
print(f"Desvío estandad: {desvio_e:.2f}")

#ARREGLOS: Matrices unidimensionales
lista_numeros2 = [1,10,100,3,75,36,79,11]
arr_numeros2 = np.array(lista_numeros2)
print(arr_numeros2)
print(type(arr_numeros2))
print(arr_numeros2[0])
print(arr_numeros2[-1])