
'''
Clase:        Clase 10 -- Manejo de Matrices
Tema:         Manejo de Matrices
Ejercicio:    10.3.2 -- Juego del entorno

Descripción:  Dada una matriz binaria ingresada por el
              usuario, verifica para cada celda de una
              matriz binaria cuántos elementos con valor
              de 1 hay en las celdas vecinas (arriba, abajo,
              izquierda, derecha, diagonales)

Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-06-14
Estado:       [Terminado]
'''

def leer_matriz(): # Creas una funcion que guarda los datos de la matriz
    n = int(input("Ingrese el número de filas: "))
    m = int(input("Ingrese el número de columnas: ")) #Pedis al usuario que ingrese el numero de filas y columnas 
    matriz = [] # Creas una lista que va a guardar los datos de la matriz
    print("Ingrese la matriz fila por fila (solo 0 y 1, separados por coma):")
    for k in range(n):
        fila = list(map(int, input().strip().split())) # El usuario ingresa la secuencia binaria de cada fila
        matriz.append(fila) #Se agrega cada fila a la matriz
    return matriz

def contar_vecinos1 (matriz):
    n = len(matriz) # Se determina el numero de filas     
    m = len(matriz[0]) #Se determina el numero de columnas    
    resultado = [[0]*m for y in range(n)]  # Creamos una matriz vacía para guardar los resultados de las sumas

    direcciones = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)] #Las busque en Internet, pero representan las 8 direcciones

    for i in range(n):         
        for j in range(m): # Hacemos un for anidado que recorre cada celda de la matriz
            suma = 0 # Nuestra variable de suma de forma predeterminada es cero
            for dx, dy in direcciones:  # El programa recorre cada direccion vecina
                ni, nj = i + dx, j + dy  # El programa calcula la posicion del vecino
                if 0 <= ni < n and 0 <= nj < m:  # Se asegura que la posicion del vecino este dentro de los limites de la matriz
                    suma += matriz[ni][nj]       # En caso el vecino si sea 1, la variable suma aumenta en 1
            resultado[i][j] = suma  # Se guarda la suma en la matriz resultado

    return resultado


def imprimir_matriz(matriz):
    for n in matriz: # Recorre cada fila de la matriz
        print(n) # Imprime cada fila de la suma


matriz = leer_matriz()
resultado = contar_vecinos1 (matriz)
print("Matriz de suma de vecinos con valor 1132was:")
imprimir_matriz(resultado)

