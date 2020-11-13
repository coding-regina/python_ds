import numpy as np

# 1. Crear un vector con valores dentro del rango 10 a 49
array1 = np.arange(10,50)
print(array1)
print('')

# 2. Invertir el vector creado en el ejercicio 1.
# EXPLICACIÓN DE PAO LA GENIA
# Regi, me dejaste pensando en lo de invert y para entenderlo hay que cachar
# que ver que significa sacar el complemento del binario de un numero. Por ejemplo:
# bin(9) es '0b1001'
# Para sacar el complemento (~), primero toma el binario del numero y *flipea*
# los bits de derecha a izquierda hasta que encuentra el primer 0 (siendo
# este 0 el ultimo que *flipea*). Luego invierte el signo.
# Tomamos el binario del 9 -> '0b1001'
# index -1: 1 -> 0
# index -2: 0 -> 1 y paramos
# int('0b1010', base=0) es 10
# por lo que ~9  es igual a -10
print('Invert  : ', np.invert(array1))
print('')
print('Negative: ', np.negative(array1))
print('')
print('Flip: ', np.flip(array1))
print('')
print('::-1: ', array1[::-1])

# board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
# print(board)


# LECTURAS
# https://programacionpython80889555.wordpress.com/2019/09/17/metodo-sencillo-para-crear-matrices-con-python-y-numpy/
# https://riptutorial.com/es/numpy/example/31052/numpy-matriz-n-dimensional--la-ndarray
# https://www.datacamp.com/community/tutorials/python-numpy-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=332602034361&utm_targetid=aud-392016246653:dsa-473406585115&utm_loc_interest_ms=&utm_loc_physical_ms=1000073&gclid=Cj0KCQiAhZT9BRDmARIsAN2E-J05xVVyRmIJQloFOIY36hypdd3BpwQp45dhIPq81b9YtlJfJYeOMyAaAvEdEALw_wcB
# https://www.analyticslane.com/2019/12/11/numpy-basico-como-invertir-arrays-de-numpy/#:~:text=Invertir%20matrices%20en%20Numpy&text=flip()%20dispone%20de%20la,indicar%20con%20el%20valor%201.
# https://www.analyticslane.com/2019/12/11/numpy-basico-como-invertir-arrays-de-numpy/