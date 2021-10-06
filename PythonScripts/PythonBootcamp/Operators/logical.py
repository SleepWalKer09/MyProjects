#operadores logicos
#1 and
#2 or 
#3 not

#todas las opciones deben ser verdades
if (3>2) and (4>2):
    print("True")

#minimo una opcion debe ser verdadera
if (3>2) or (4>2):
    print("True")

#las opciones deben ser falsas para que sea verdadero
a = not(3>2)
print(a)
b = not(2>3)
print(b)
