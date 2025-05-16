Consumoenergia=int(input("Ingresa su consumo de energia: "))
Impuesto=0

if Consumoenergia <= 100:
    print("No debes pagar nada de impuestos")
    
elif 101 < Consumoenergia <=200:
    Impuesto=0.5*Consumoenergia
    print("Debe pagar", Impuesto, "por su consumo")

else:
    Impuesto=0.7*Consumoenergia
    print("Debe pagar", Impuesto, "por su consumo")