#Funciones sin nombre
#sintaxis ---> lambda argumentos: expresion
#argumenosilimitados, PERO SOLO UNA LINEA DE CODIGO
#NO necesitan "return"

#ejericio 1: usando lambdas, saber si una palabra es palindroma
###################
#FORMA TRADICIONAL#
###################
def palindorme(string):
    return string == string[::-1]

print(palindorme('ana'))

###############
#Forma anonima#
###############
pali = lambda string: string == string[::-1] #significa que aplica slices para dar vuelta al string y pregunta si el string es igual al string al reves
print(pali('ana')) #el resultado sera "true" ya que si se cumple la expresion




