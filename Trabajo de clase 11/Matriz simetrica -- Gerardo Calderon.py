
'''
Clase:        Clase 10 -- Manejo de Matrices
Tema:         Manejo de Matrices
Ejercicio:    10.3.1 -- Matriz simetrica

Descripción:  Dada una matriz cuadrada ingresada por el
              usuario, comprueba si la matriz cuadrada es
              simétrica respecto a su diagonal principal.

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
        break
matriz.append(fila)
    
essimetrico=False  # Creamos la variable booleana con la que trabajaremos la simetria

for i in range(n):
        for j in range(n): #Hacemos un for dentro de otro for que usaremos como iterables que recorran las columnas y filas
            if matriz[i][j] == matriz[j][i]: # Condicionamos que si la celda i,j es igual que la celda j,i la matriz es simetrica
                essimetrico=True
                break
            else:
                essimetrico=False
                break # Si no es igual, se rompe el bucle, y pues la variable se mantiene en False

if essimetrico== True:
    print("La matriz es simetrica")
elif essimetrico== False:
    print("La matriz no es simetrica")
    
