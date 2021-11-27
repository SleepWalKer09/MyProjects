#Funciones que reciben de parametros otras funciones y hace algo con ella
#3 tipos: filter, map y reduce
########################################################################################################################
#EJEMPLO FUNCION FILTER
#La funcion "filter" recibe como parametro funcion(anonima o no) y un iterable(cualquier elemento que pueda recorrerse)
#filter devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.

#De una lista de numeros, filtrar los numeros impares
mi_lista = [1,4,5,6,9,12,13,19,21,26]
#funcion anonima que recibe como parametro una variable x y regresa el resultado de la operacion x%2!=0 como true o false
#agregando "list" que envuelva a toda la funcion se puede obtener la lista esperada
odd = list(filter(lambda x: x%2 != 0, mi_lista))#funcion lambda que recibe cada uno de los elementos de la lista que es el segundo parametro de la funcion filter y se transforma a lista
print(odd)
########################################################################################################################
#EJEMPLO FUNCION MAP
#funcion "map"
#Map funciona muy parecido a filter, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

#de una lista de numeros, calcular sus potencias
mi_lista1 = [1,2,3,4,5]
#misma estructura que filter
cuadra = list(map(lambda x: x**2, mi_lista1))#lambda que recibe parametro x y regresa x^2 guardandolo en una nueva lista llamada cuadra
print(cuadra)
########################################################################################################################
#EJEMPLO FUNCION REDUCE
#REDUCE, NO viene por default dentro de python
#Reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

#de una lista de numeros, obtener la multiplicacion total de la lista
from functools import reduce
mi_lista2 = [2,2,2,2,2]
#misma estructura que filter
total = reduce(lambda a,b: a*b, mi_lista2)# lambda que multiplica el primer y segundo elemento de la lista por cada iteracion
print(total)