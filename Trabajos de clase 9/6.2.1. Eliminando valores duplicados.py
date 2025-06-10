'''
Clase:        Clase 6 -- Manejo de Listas
Tema:         Manejo de Listas
Ejercicio:    6.2.1 -- Eliminando Valores Duplicados

Descripción:  Dada una lista ingresada por el usuario,
              elimina los elementos duplicados
              manteniendo la primera aparición de cada
              número.
              
Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-06-2
Estado:       [Terminado]
'''

numerosusuario = input("Ingresa la lista de numeros con espacio entre numeros: ")
numeroslista = numerosusuario.split()
numerosenteroslista = [int(n) for n in numeroslista]

resultado = []

for n in numerosenteroslista:
    if n not in resultado:
        resultado.append(n)

print("La lista de numeros sin duplicados es:", resultado) 