'''
Clase:        Clase 10 -- Manejo de Matrices
Tema:         Manejo de Matrices
Ejercicio:    10.2.1 -- Diagonal Principal y Secundaria

Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, crea dos listas, una con los
              elementos de la diagonal principal y la otra
              con los elementos de la diagonal
              secundaria.

Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-06-14
Estado:       [Terminado]
'''


# El usuario ingresa el tamaño de la matriz, que solo puede ser un numero entero n
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

# Inicializar la matriz teniendo en ceunta el numero dado por el usuario
matriz = [] #Se crea una lista llamada matriz, que almacenara la matriz
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n): #Se crea la variable i, que representa a cada numero de la matriz, y n el tamaño de la fila           
    fila = list(map(int, input().split(","))) # El usuario ingresa los numeros de la fila, estos se separan individualemnte con el split
                                           #y se les aplica una funcion de enteros con el map, y se ingresa a la lsita matriz
    if len(fila) != n:
        print("Cada fila debe tener", n, "elementos.") # Solo se condiciona en caso la fila tenga mas o menos elementos que los ingresados
        exit(1)
    matriz.append(fila)


diagonal_principal = [matriz[i][i] for i in range(n)] # Creamos la variable de la diagonal, y se retoma cada fila i con su respectiva columna i
diagonal_secundaria = [matriz[i][n - 1 - i] for i in range(n)] # Similar para la diagonal secundaria, solo que aca tomamos el ultimo i respectivo a la primera columna i

print("Diagonal principal:", diagonal_principal) # Imprimimos la diagonal principal
print("Diagonal secundaria:", diagonal_secundaria) #Imprimimos la diagonal secundaria

#--- Alumno: Gerardo Andre Calderon Castillo --

