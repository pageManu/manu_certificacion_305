try:
    numero1=int(input("Ingresa el primer numero"))
    numero2=int(input("Ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("DIVISION ENTRE CERO MAMASTE PERRO")
except ValueError:
    print("EL CECYTEM TE HA CAMBIADO YA NO ERES LA KABRA")


