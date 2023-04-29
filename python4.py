genero = input("Ingrese su genero (M/F):")
edad = int (input("Ingrese du edad:"))

if genero == "M" and edad >= 18:
    print("Puede participar")
elif genero == "F" and edad >= 18:
    print("Puede participar")
else:
    print("No puede participar")

    
