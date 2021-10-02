#cuenta el numero de string de un string 
a = 'hello world'
print(len(a))
#########################################################
#cuenta el numero de veces que se repite algun caracter
def frecuencia(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(frecuencia('google.com'))
#################################################################
#string con 2 primeros y 2 ultimos caracteres dados de un string
def cadena(str):
    if len(str) < 2:
        return ''
    return str[:2] + str[-2:]
print(cadena('apexCompany'))
print(cadena('apexCo'))
print(cadena('a'))
##################################################################
#ordenar alfabeticamente un string
def AlphabetSoup(str): 
    str = "".join(sorted(str))
    # code goes here 
    return str
print(AlphabetSoup('raw_input'))
###################################################################
#tomar 2 parametros y regresar si el num2 es mayor que el primero,
def CheckNums(num1,num2): 
    if num2 > num1:
        return 'true'
    elif num2 < num1:
        return 'false'
    else:
        return '-1'
    
# keep this function call here  
print(CheckNums('23','12'))
#######################################################################
#imprimir del 1 al 15 
i = 1
j = 15
while(i<=j):
    print(i)
    i+=1
#########################################################################
#cada multiplo de 3 se pone la palabra "fuzzy" del 1 al 15
#cada multiplo de 5 se pone la palabra "buzz" del 1 al 15
#si es multiplo de ambos se pone la palabra "fuzzybuzz"
i= 1
j= 15
while(i<=j):
    if(i%3 == 0) and (i%5 == 0):
        print('fuzzybuzz')
    elif(i%3 == 0):
        print('fuzzy')
    elif(i%5 == 0):
        print('buzz')
    else:     
        print(i)
    i+=1
############################################################################
#diferencias entre tupla y lista
import sys
a_list = list()
a_tuple = tuple()
a_list = [1,2,3,4,5]
a_tuple = (1,2,3,4,5)
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))
##############################################################################
#remover duplicados en un array
arr = [1,2,3,1,4,2,5,3,5,1,6,1,7]
def duplicados(arr):
    return(list(set(arr)))
print(duplicados(arr))
###############################################################################
#Have the function CorrectPath(str) read the str parameter being passed,
# which will represent the movements made in a 5x5 grid of cells starting from the top left position.
#  The characters in the input string will be entirely composed of: r, l, u, d, ?.
#  Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down.
#  Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top 
# left of the grid all the way to the bottom right without touching previously travelled on cells in the grid. 

def CorrectPath(s): #bruteforce ftw!
	import random
	while True:
		route=[]
		tracepos=[]
		x=1;y=5;answer=1
		for i in s:
			if i=="?":i=random.choice("lrud")
			if i=="u":y+=1
			elif i=="d":y-=1
			elif i=="r":x+=1
			elif i=="l":x-=1
			if (x,y) in tracepos:
				answer=0
				break
			else: tracepos.append((x,y))
			route.append(i)
			if x==6 or x==0 or y==0 or y==6:
				answer=0
				break
		if x==5 and y==1 and answer==1:
			return "".join(route)

print (CorrectPath('drdruurrdddd'))
##################################################################################################################
#serie defibonacci FORMULA: fn = fn-1 + fn-2
#iterativo
def fiib(n):
    a = 0
    b = 1
    for k in range(n):
        c = a+b
        a=b
        b=c
    return b
for x in range(20):
    print(fiib(x))

#recursaiva 
def fibr(n):
    if (n<2):
        return n
    return fibr(n-1) + fibr(n-2)

for x in range(20):
    print(fibr(x))
####################################################
#promedio de datos dados por un usuario

a = int(input("de que tamaño sera?: "))

i= 0
acum = 0
for i in range(a):
    x = int(input("Di los numeros: "))
    acum = acum+x
    i+=1

prom = acum/a
print("Tu promedio es: ",prom)
#####################################################
#saber si un numero es par
a = int(input("numero: "))
b = a%2
if (b == 0):
    print("Es par")
else:
    print("Es impar")
#####################################################
#####################################################
#cada multiplo de 3 se pone la palabra "fuzzy" hasta el 100
#cada multiplo de 5 se pone la palabra "buzz" hasta el 100
#si es multiplo de ambos se pone la palabra "fuzzybuzz"

for x in range(50):
    result = ""
    if(x%3 == 0):
        result = "fizz"
    if(x%5 == 0):
        result = "buzz"
    if(result == ""):
        print(x)
    else:
        print(result)

##############################################################################
#escribe una funcion que cheque todas las permutaciones generen un palindomo
#e.g civic

def check_palindome(str_input: str):
    chars = {}
    for char_input in str_input:
        if char_input in chars.keys():
            chars[char_input] +=1
        else:
            chars[char_input] = 1

    counter = 0
    for char_value in chars.values():
        if char_value % 2 != 0:
            counter +=1
        if counter > 1:
            return False

    return True

print(check_palindome("civic"))
print(check_palindome("ivicc"))
print(check_palindome("civil"))
print(check_palindome("livci"))

#################################################################################
# problema de parentesis, input cadena de caracteres, revisar si tiene un orden correcto

def cadena_parentesis(cadena):
    pila =[]
    parentesis = {'(':')','[':']','{':'}'}

    for c in cadena:
        if c in parentesis:
            pila.append(c)
       #si pila vacia o caracter a caracter de cierre no corresponde
        elif len(pila) == 0 or c != parentesis[pila.pop()]:
            return False#son parentesis diferentes
    #un solo parentesis de aparteruta
    return len(pila) == 0

print(cadena_parentesis("()[]{}"))
print(cadena_parentesis("()[{}"))
print(cadena_parentesis("{[()]}"))
print(cadena_parentesis("(}{"))