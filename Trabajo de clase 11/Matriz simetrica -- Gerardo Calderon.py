
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

# Inicializamos la matriz teniendo en cuenta el numero dado por el usuario
matriz = [] #Se crea una lista llamada matriz, que almacenara la matriz
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n): #Se crea la variable i, que representa a cada numero de la matriz, y n el tamaño de la fila           
    fila = list(map(int, input().split(","))) # El usuario ingresa los numeros de la fila, estos se separan individualemnte con el split
                                           #y se les aplica una funcion de enteros con el map, y se ingresa a la lista matriz (reomado de Chat GPT)
    if len(fila) != n:
        print("Cada fila debe tener", n, "elementos.") # Solo se condiciona en caso la fila tenga mas o menos elementos que los necesarios
        exit(1)
    matriz.append(fila)
    
essimetrico = True  # Suponemos que es simétrica hasta encontrar lo contrario

for i in range(n):
    for j in range(n): #Se usa un for anidado para evaluar tanto filas como columnas 
        if matriz[i][j] != matriz[j][i]: # Condicionamps que si el valor de la celda i, j no es el mismo que
                                         # el de la celda j,i la matriz no es simetrica
            essimetrico = False
            break
    if not essimetrico:
        break

if essimetrico:
    print("La matriz es simetrica")
else:
    print("La matriz no es simetrica") # Se condiciona para determinar que se va a imprimir, si es o no es simetrica
    
    
#--- Alumno: Gerardo Andre Calderon Castillo --
    
    
