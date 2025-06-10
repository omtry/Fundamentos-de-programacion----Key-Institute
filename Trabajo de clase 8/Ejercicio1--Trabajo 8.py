'''
Clase:        Clase 5 -- Bloques Iterativos
Tema:         Bloque Iterativo
Ejercicio:    5.4.1 -- Adivina el numero

Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
              El programa debe seguir pidiendo números hasta que acierte. En cada
              intento fallido el programa notificará al usuario si el número secreto es
              mayor o menor al último valor ingresado
              
Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-05-28
Estado:       [Terminado]
'''


import random

Numeroaadivinar = random.randint(1, 100)

while True:
    try:
        Intentoadivinar = int(input("Intenta adivinar el numero entre el 1 y el 100: "))

        if Intentoadivinar < Numeroaadivinar:
            print("El número secreto es mayor que el numero ingresado.")

        elif Intentoadivinar > Numeroaadivinar:
            print("El numero secreto es menor al ingresado.")

        else: 
            print("¡Felicidades, adivinaste el numero secreto!")
            print("Fin del juego")
            break

    except ValueError:
        print("Solo los enteros son validos")