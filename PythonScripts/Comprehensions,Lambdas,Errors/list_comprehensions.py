###############
#Instrucciones#
###############
#Crear una lista con los cuadrados de los primeros 100 numeros naturales
#Solo eliminar numeros que no son divisibles entre 3
#----------------------------------------------------------------------
#MODO CLASICO
def run():
    squares = []
    for i in range(1,101):        
        if i % 3 != 0:
            squares.append(i**2)
    print(squares)

#----------------------------------------------------------------------
#MODO Comprehensions
#Misma funcion anterior pero usando "list comprehensions"

# [element FOR element IN iterable IF condition]

#element                 = representa cada uno de los elementos a poner en la nueva lista
#for element in iterable = ciclo a partir del cual se extraeran elementos de otra lista o cualquier iterable
#if condition            = condicion opcional para filtrar elementos del ciclo

#Para cada elemento en el iterable guardar el elemento solo si se cumple la condicion
def run():
    cuadrados = [i**2 for i in range(1,101) if i%3 != 0]


#----------------------------------------------------------------------
#RETO CLASE
#Usando list comprehension crear una lista de todos los multiplos de 4 que a su vez tambien son multiplos de 6 y de 9 hasta 5 digitos
def run():
   
    reto = [i for i in range(1, 100000) if i % 36 == 0] #36 es divisible entre 4,6 y 9
   # reto = [i for i in range(1,100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(reto)



if __name__ == '__main__':
    run()