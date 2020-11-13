import numpy as np
from scipy import stats
array = np.array([1,4,19,10,5])

array_2 = np.add(array,4)
print(array_2)

array_3 = np.subtract(array,2)
print(array_3)

array_5 = np.multiply(array,3)
print(array_5)

array_6 = np.divide(array,2)
print(array_6)

array_7 = np.floor_divide(array,2)
print(array_7)

array_8 = np.power(array,2)
print(array_8)

array_9 = np.mod(array, 2)
print(array_9)

array_20 = np.array(([1, 4, 19, 10, 5], [3, 9, 10, 8, 8]))
print('...')
array_21 = np.append(array_20, ([0, 0, 0, 0, 0], [1, 1, 1, 1, 1]), axis=0)
print(array_21)
print('...')
array_22 = np.append(array_20, ([0, 0, 0, 0, 0], [1, 1, 1, 1, 1]), axis=1)
print(array_22)

print('...')
array_40 = np.array(([1, 4, 19, 10, 5], [3, 9, 10, 8, 8]))
array_41 = np.copy(array_40)
print(array_41)
print('...')
array_42 = array_40[:]
print(array_42)
print('...')
print(id(array_41))
print(id(array_42))
print(id(array_40))

a = [[0,1,2,3,4,5],
     [10,11,12,13,14,15],
     [20,21,22,23,24,25],
     [30,31,32,33,34,35],
     [40,41,42,43,44,45],
     [50,51,52,53,54,55]]
print('...')
print(a)
print('...')
np.random.seed(0)
b = np.random.randint(0, 55, (6,6))
print(b)
print('...')
a[0,3:5]
print('...')
a[4:,4:]
print('...')
a[:,2]
print('...')
a[2::2,::2]
print('...')