#Cadenas y concatenacion con (+)
cadena1='Hola'
cadena2='Mundo'
multilinea=""""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
eco="ja"*3
print(eco)
tu_nombre='xxManu'
#convertir mayuscula
print(tu_nombre.upper())
#Mayuscula a minuscula
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#Formato de contatenar cadenas (F-String)
edad=+18
Nombre='xxManu'
mensaje=f"Hola, me llamo {Nombre} y tengo\n {edad} años"
print(mensaje)
texto= "¡¡¡Felicidades eres un ganador a un viaje a mamitas puebla!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
oracion=" Aprender python es malo"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
ncadena="a1"
print(ncadena.isalpha())#True
print(ncadena.isdigit())#False