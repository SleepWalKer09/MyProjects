#instrucciones:
# 1. Simular las caras de un dado que se tiraran aleadoriamente
# 2. Debe tener 6 caras
# 3. Debe ser recursivo

import random
#numeros aleatorios enteros del 1 al 6
x = "si"
while x == "si":
    number = random.randint(1,6)
    if (number == 1):
        print("Obtuviste el numero 1")
        print("")
        print("----------") 
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")
        print("")
    if (number == 2):
        print("Obtuviste el numero 2")
        print("")
        print("----------") 
        print("|        |")
        print("| 0    0 |")
        print("|        |")
        print("----------")
        print("")
    if (number == 3):
        print("Obtuviste el numero 3")
        print("")
        print("----------") 
        print("|    0   |")
        print("|    0   |")
        print("|    0   |")
        print("----------")
        print("")
    if (number == 4):
        print("Obtuviste el numero 4")
        print("")
        print("----------") 
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")
        print("")
    if (number == 5):
        print("Obtuviste el numero 5")
        print("")
        print("----------") 
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")
        print("")
    if (number == 6):
        print("Obtuviste el numero 6")
        print("")
        print("----------") 
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")
        print("")
    #recursividad
    x = input("¿Girar nuevamente?(si/no)\n")