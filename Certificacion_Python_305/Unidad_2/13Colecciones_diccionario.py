#Creando un diccionario en python 
persona={
    "nombre": "xxManu",
    "edad":18,
    "profesion":"Ingenieria",
    "estudiante":False
}
print(persona)
#accediendo a un valor especificico
print(persona["edad"])
#se puede usar el metodo .get()
#Es util por que no da el error si la clsve no existe
print(persona.get("profesion"))
#Codificar un valor existente
persona["edad"]=29
print(persona.get("edad"))
#agregar un par (clave.:valor)
persona["ciudad"]="Ciudad Gotica"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"{clave}:{valor}")