numerousuario=int(input("Ingrese un numero para ver si es magico: "))

if numerousuario % 7==0 and numerousuario % 5 !=0:
    print("Magico")

else:
    print("Normal")