'''
Clase:        Clase 6 -- Manejo de Listas
Tema:         Manejo de Listas
Ejercicio:    6.3.1 -- Numeros Lideres

Descripción:  Un número en una lista es "líder" si es
              estrictamente mayor que todos los
              elementos a su derecha. Dada una lista de
              números ingresada por el usuario, imprime
              todos los números líderes.
              
Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-06-2
Estado:       [Terminado]
'''

Listanumeros = input("Ingresa una lista de numeros para determinar los numeros lideres: ")
Numeroslista=Listanumeros.split()
todolisto = [int(x) for x in Numeroslista]

Numeroslider = []
for n in range(len(todolisto)):
    actual = todolisto[n]
    if all(actual > x for x in todolisto[n+1:]):
        Numeroslider.append(actual)

print("Los numeros lider de la funcion son:", Numeroslider) 