contraseña=input("Ingresa tu contraseña: ")
if len(contraseña) >= 8 and any(letra.isdigit() for letra in contraseña) and any(letra.isupper() for letra in contraseña):
    print("Contraseña Segura")

else:
    print("Contraseña no segura")

