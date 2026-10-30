try:
    alumnos = ["xxvane", "xxManu", "XXMonse", "XXSaul", "XXPaola", "xxRosalia", "XXFran", "XXADRI", "XXmax", "XXCarliwis"]
    
    calificaciones = [6.0, 10.0, 10.0, 9.0, 8.0, 4.0, 5.0, 6.0, 9.0, 2.0]
    
    print(alumnos[1], calificaciones[1])
    print(alumnos[2], calificaciones[2])
    print(alumnos[3], calificaciones[3])  
    print(alumnos[4], calificaciones[4])
    print(alumnos[5], calificaciones[5])
    print(alumnos[6], calificaciones[6])
    print(alumnos[7], calificaciones[7])
    print(alumnos[8], calificaciones[8])
    print(alumnos[9], calificaciones[9])
    
except IndexError:
    print("Indice Incorrecto")
except TypeError:
    print("Error de tipo de dato")