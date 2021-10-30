#guardar el cubo de los 100 primeros numero naturales
#no guardar numeros que sean divisibles entre 3
#-----------------------------------------------------
#MODO CLASICO

def run():
    my_dict = {}
    for i in range(1,101):        
         if i % 3 != 0:
             my_dict[i] = 1**3
    print(my_dict)


# #----------------------------------------------------
# # DICTIONARY COMPREHENSIONS
# #diferencia con "list comprehension": 
#     # 1. llaves en lugar de corchetes
#     # 2. en el elemento se pone nombre y valor

# #{ key : value for value in interable if condition}

# # key: value            = cada una de las llaves y valores a poner en el nuevo diccionario
# # for value in iterable = ciclo a partir del cual se extraeran elementos de cualquier iterable
# # if condition          = condicion OPCIONAL para filtrar los elementos del ciclo

def run():
    my_dict = {i : i**3 for i in range(1,101) if i%3 != 0}


#-------------------------------------------------------
#RETO CLASE
#usando comprehensions crear un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores

def run():
    reto = {i: round(i**(0.5),2) for i in range (1, 1001)}
    print(reto)


if __name__ == '__main__':
    run()
