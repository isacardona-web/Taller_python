
#creacion de variables
nombre = "Isabel"
documento = 123 
direccion = "Medellin cra 62"

tiene_deuda = True 

print(nombre) 

print("CONCATENACION USANDO +")
print("=" * 30)

print("Mi nombre es: " + nombre + " y mi documento es: " + str(documento))

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"nombre : {nombre} Documento : {documento} direccion : {direccion}  ") 

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""

-nombre : {nombre}
-documento : {documento}
-direccion : {direccion}
-tiene deuda : {tiene_deuda}


""")

print(f"\n Hola, \n{nombre}")