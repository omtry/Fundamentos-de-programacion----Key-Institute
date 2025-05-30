numerosusuario = input("Ingresa la lista de numeros con espacio entre numeros: ")
numeroslista = numerosusuario.split()
numerosenteroslista = [int(n) for n in numeroslista]

resultado = []
numerosyaaparecidos = set()
for n in numerosenteroslista:
    if n not in numerosyaaparecidos:
        resultado.append(n)
        numerosyaaparecidos.add(n)

print("La lista de numeros sin duplicados es:", resultado)