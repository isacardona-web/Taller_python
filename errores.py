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


    try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")  

    while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   # sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

# Ejercicio 5: raise — lanzar una excepción personalizada
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")
