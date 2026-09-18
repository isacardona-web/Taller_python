""" or i in range(2,11,2):
    print(f" {i}: Hi girl 😘") 
    """

""" mensaje = input("Write your message :")
recepcion = int(input("How many times do you want to repeat the message? :"))

for i in range(recepcion): 
    print(f"{i+1}: {mensaje}")
    """
#Ask the student name
#Ask to the teacher how many scores do you want to register 
#Make the average of the scores and print the result with the student name
#average >=3.5 show "Approved" else show "Failed" 





""" average = 0
for i in range(num_scores):
    score=float(input(f"Write the score {i+1}: "))
    
    if score not in range(0,5):
        print("The score is invalid")
        break 

        
    average += score

final_score = average/num_scores

if (average/num_scores) >= 3.5:
    print(f"student_name {student} - average: {final_score} - Approved 👌")
else:
    print(f"student_name {student} - average: {final_score} - Failed 😔")
    """

while True:



    menu =int(input(""" 


    Seleccione opcion a realizar :
    1. Sumar
    2. Restar
    3. Salir    
    
     """))
    

    if menu == 1:
        n1= int(input("Ingrese el primer numero: "))
        n2= int(input("Ingrese el segundo numero: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif menu == 2:
        n1= int(input("Ingrese el primer numero: "))
        n2= int(input("Ingrese el segundo numero: "))
        print(f"El resultado de la suma es: {n1-n2}")
    elif menu == 3:
        print("Saliento del programa")
        break
    else:
        print("Opcion invalida")
        
    
    

