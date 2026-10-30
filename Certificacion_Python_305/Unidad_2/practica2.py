Dias_habiles=( "lunes","miercoles","Viernes")
Dias=input("Ingresa el dia de tu asistencia: ")
if Dias in Dias_habiles:
    print("Registro exitoso")
else:
    print("Dia fuera de servicio")
