promedio=[6,7,8,9,10]
#1. Encontrar el promediomas bajo usando ciclo for
#Suponemos incialmente que el promedio mas bajo es el primero 
promedio_bajo=promedio[0]
promedio_alto=promedio[0]
for contador in promedio:
   if contador<promedio_bajo:
        promedio_bajo=contador
   elif contador > promedio_alto:
        promedio_alto=contador
print(promedio_alto)
print(promedio_bajo)
