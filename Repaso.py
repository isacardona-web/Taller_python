print("=== Tienda la gran esquina ===")

print("por favor ingrese la siguiente información: \n")
cliente =input("Nombre del cliente: ")
producto =input("Nombre del producto: ")
cantidad =int(input("Cantidad: "))
precio =float(input("Precio: "))
domicilio =input("¿La compra es por domicilio? (si/no): ")

if domicilio.upper() =="NO":
    print("=== RESUEMN DE LA COMPRA ===")
    print(f"""
    -Cliente : {cliente}
    -Producto : {producto}
    -Cantidad : {cantidad}
    -Precio : {precio}
    -total a pagar : {cantidad * precio}

    GRACIAS POR SU COMPRA.

 
    """ )

If dimicilio.upper() =="NO":
elif domicilio.upper() =="SI":
    print("=== RESUEMN DE LA COMPRA ===")
    print(f"""
    direccion de domicilio : {input("Ingrese municipio de emvio (Medellín, Bello, Itagui): ")}


 
    """ )


    valor_domicilio=0    
if direccion.lower()=="medellin":
    valor_domicilio=5000
elif direccion.lower()=="bello":
    valor_domicilio=8000
elif direccion.lower()=="itagui":
    valor_domicilio=10000
else:
    print("Lo sentimos, no realizamos envíos a esa dirección.")
    
    #Resumen de la venta
    print("=== RESUEMN DE LA COMPRA ===")
    print(f"""
    -Cliente : {cliente}
    -Producto : {producto}
    -Cantidad : {cantidad}
    -Precio : {precio}
    -domicilio : {valor_domicilio}
    -total a pagar : {valor_domicilio + (cantidad * precio)}

    GRACIAS POR SU COMPRA. 

else: 
    print("opcion invalida.")