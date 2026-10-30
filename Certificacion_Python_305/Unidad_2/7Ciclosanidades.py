#Ciclo externo para el numero de la base de la tabla
for i in range(1,4):
    print(f"---Tabla del {i}")
    #Ciclo interno para multiplicar del 1 al 20
    for  j in range (1,10):
    # 1 (i) x 1 (j) =1
        print(f"{i} x {j} = {i*j} " )
        #AQUI SALE DEL CICLO EXTERNO
    print(f"AQUI TERMINA LA TABLA DEL{i}")
    #AQUI SE ACABA EL CICLO EXTERNO