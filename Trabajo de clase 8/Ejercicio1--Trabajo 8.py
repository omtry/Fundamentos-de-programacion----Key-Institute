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