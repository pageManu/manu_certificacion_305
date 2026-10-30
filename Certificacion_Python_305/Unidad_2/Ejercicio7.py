#El mapa del Tesoro
mapa=[
    [".",".",".","."],
    [".",".","b","."],
    [".",".",".","X"],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Recorriedo la matriz con ciclos anidados
#Ciclo externo para manejar filas(i)
for i in range(filas):
    #Ciclo interno para manejar columnas(j)
    for j in range(columnas):#i<4
        #Verificamos si encontramos el tesoro
        if mapa[i][j]=="X":
            print(f"Tesoro encontrado en la posicion [{i}][{j}]")
        if mapa[i][j]=="b":
                    print(f"Tesoro encontrado en la posicion [{i}][{j}]")