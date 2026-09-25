lista_prodcuto=[] #lista en blaaco
cantidad=int(input("cantidad de productos a comprar: "))

for i in range(cantidad):     
    producto=input(f"Ingrese el nombre del producto: {i+1}: ")

    lista_prodcuto.append(producto)
print(f"Los productos comprados son: {lista_producto}") 
