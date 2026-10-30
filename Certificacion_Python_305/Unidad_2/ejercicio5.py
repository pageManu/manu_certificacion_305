Carrito=[]
cantidad=int(input("¿Cuantosproductos quieres agregar al carrito"))
for contador in range (cantidad):
    producto=input(f"Ingresa el producto: {contador+1}")
    Carrito.append(producto)
print("\nTu lista de compra es:")
print(Carrito)