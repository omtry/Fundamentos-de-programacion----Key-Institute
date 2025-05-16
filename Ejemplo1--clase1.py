Totalcuenta=float(input("Cual fue el total de tu cuenta: "))
Propina=int(input("Que propina daras: "))
Propinareal=round(Totalcuenta * (Propina/100),2)
total = Totalcuenta + Propinareal
print("El total de tu cuenta fue $",Totalcuenta)
print("Tu propina sera $",Propinareal)
print("El total de la cuenta con propina (",Propina,"%) fue: $",total)
