import numpy as np

#Matriz a partir de una lista
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

#Crear una matriz de ceros
zeros = np.zeros(5)
print(zeros)

#Crear una matriz de unos
ones = np.ones(5)
print(ones)

#Suma de matrices
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
resultado = arr1 + arr2

#Multiplicacion de matrices
resultado2 = arr1 * arr2

#Broadcasting con un escalar
arr = np.array([1, 2, 3])
result = arr + 5

#Difusion de matrices unidimensionale sy bidimensionales
arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])
result = arr1 + arr2

#Segmentacion
arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]


# Indexación booleana
arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask] # Recupera los elementos donde la condición es verdadera: [3, 4, 5]

#Indexacion de matrices enteras
arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 

#Concatenacion y division:

#Concatenación
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3) # Divide la matriz en 3 partes iguales