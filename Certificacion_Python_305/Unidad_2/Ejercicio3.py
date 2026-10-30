Colores=["Negro","rojo","verde","azul","turquesa,","celeste","xxRafita"]
color=input("Ingresa el Color:")
encontrado=False
for contador in Colores:
    print(contador)
    #Si el color actual es "Rojo", detener el bucle
    if contador==color:
        print("Color encontrado! Saliendo del bucle")
        encontrado=True
        break
    if not encontrado:
        print("El color,",color, "no se encontro ")