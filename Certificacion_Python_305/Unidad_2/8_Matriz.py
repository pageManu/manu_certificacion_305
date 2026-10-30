matriz=[
    [5,8,6],#Fila1 x 3 columnas
    [3,9,4]#Fila 2 x 3 columnas
]
#Obteniendo el numero total de filas y columnas
filas=len(matriz)
columnas=len(matriz[0])
#Ciclo externo para los idices de las filas(i)
for i in range (filas):
    #Ciclo interno para los indices de las columnas(j)
    for j in range(columnas):
        print(f"Posicion[{i}][{j}]={matriz[i][j]}")