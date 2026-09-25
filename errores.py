""" while True:
    try:
        nota=float(input("ingresa una nota: ")) 
    except ValueError:
        print("ingresa una nota valida ") """

"""while True:
    try:
        cantidad_notas =int(input("cuantas notas quieres registrar: "))
        lista_notas=[]
        for i in range(cantidad_notas):
            try:
                nota=float(input("Ingrese una nota"))
                lista_notas.append(nota)
            except ValueError:
                print("nota invalida")    
        print("notas registradas: ", lista_notas)
        promedio=sum(lista_notas)/len(lista_notas)
        print(f"promedio: {promedio}")

        nota_final = promedio

        if promedio <=3:
            else:
                print(f"su nota es basico:")

        if promedio <=4:
            else:
                print("su nota es aceptable:")

        if promedio <=5:
            else:
                print("su nota es bien:")        

    except ValueError:
        print("ingrese una cantidad valida")  
"""

""" try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un número entero válido.") 

"""

try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor   = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese únicamente valores numéricos.")
    
