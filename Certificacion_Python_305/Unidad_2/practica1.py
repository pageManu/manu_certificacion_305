alumnos=[]
promedio=[]
cantidad=int(input("¿Cuantos alumnos quieres ingresar"))
for contador in range (cantidad):
    producto=input(f"Ingresa los nombres: {contador+1}")
alumnos=input("Ingresa el nombre del alumno: ")
promedio=float(input("Ingresa el promedio: "))
promedio=[6,7,8,9,10]
promedio_bajo=promedio[0]
promedio_alto=promedio[0]
alumnos.append(promedio)
for contador in promedio:
   if contador<promedio_bajo:
        promedio_bajo=contador
   elif contador > promedio_alto:
        promedio_alto=contador
print(promedio_alto)
print(promedio_bajo)
print("El promdedio de",alumnos, "es:",promedio)