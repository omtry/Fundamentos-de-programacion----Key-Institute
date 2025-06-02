Listanumeros = input("Ingresa una lista de numeros para determinar los numeros lideres: ")
Numeroslista=Listanumeros.split()
todolisto = [int(x) for x in Numeroslista]

Numeroslider = []
for n in range(len(todolisto)):
    actual = todolisto[n]
    if all(actual > x for x in todolisto[n+1:]):
        Numeroslider.append(actual)

print("Los numeros lider de la funcion son:", Numeroslider) 