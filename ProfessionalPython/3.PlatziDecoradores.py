"""
Decoradores en Python:
    Closure especial que recibe una funcion como parametro otra funcion, le añade funcionalidades nuevas, 
    la vuelve a ejecutar y retorna una funcion diferente

    1. La funcion recibe una funcion input
    2. Al input se le agrega funcionalidad
    3. La funcion ejecuta la funcion input modificada
    4. La funcion retorna el resultado de la funcion input modificada
"""

#EJEMPLO CON SINTAXIS NORMAL

def decorador(func):
    def envoltura():
        print('Esto se añade a mi funcion original')
        func()
    return envoltura

def saludo():
    print('Hola!')

saludo()
#output: Hola!

saludo = decorador(saludo)
saludo()
#output:
#   Esto se añade a mi funcion original
#   Hola!


#################################################
#Ejemplo con "Sugar Sintax"

def decorador(func):
    def envoltura():
        print('Esto se añade a mi funcion original')
        func()
    return envoltura

#añade @ al decorador con el cual queramos decorar
# saludo esta decorada
@decorador
def saludo():
    print('Hola!')

saludo()