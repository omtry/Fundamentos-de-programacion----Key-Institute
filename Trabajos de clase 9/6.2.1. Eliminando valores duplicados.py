numerosusuario = input("Ingresa la lista de numeros con espacio entre numeros: ")
numeroslista = numerosusuario.split()
numerosenteroslista = [int(n) for n in numeroslista]

resultado = []

for n in numerosenteroslista:
    if n not in resultado:
        resultado.append(n)

print("La lista de numeros sin duplicados es:", resultado) 