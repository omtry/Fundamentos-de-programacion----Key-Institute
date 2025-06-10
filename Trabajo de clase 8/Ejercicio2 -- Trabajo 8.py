
'''
Clase:        Clase 5 -- Bloques Iterativos
Tema:         Bloque Iterativo
Ejercicio:    5.4.2 -- Suma de valores posicionales

Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito.

Autor:        Gerardo Andre Calderon Castillo
Fecha:        2025-05-28
Estado:       [Terminado]
'''

print("-"*25)
Numeroasumar = input("Ingrese un numero el cual reduciremos: ")
print("-"*25)
print( f"Proceso de reduccion para {Numeroasumar}")
print("-"*25)

while len(Numeroasumar) > 1: # Basicamente esta condicion es la que guia todo el programa, por que se asegura que se haga la suma hasta que el numero tenga un unico digito
    suma = sum(int(digito) for digito in Numeroasumar) # Basicamente estas haciendo que todos los digitos sean numero y que se sumen entre si
    print(f"La suma de {Numeroasumar} es: {suma}")
    Numeroasumar = str(suma)
print("-"*25)
print(f"El resultado final es: {Numeroasumar}")
print("")