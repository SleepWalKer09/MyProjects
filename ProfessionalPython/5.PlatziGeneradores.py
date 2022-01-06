"""
Sucesion de Fibonacci usando generadores
En lugar de clases, se usan funciones
En lugar de atributos, se usan variables
"""
from time import sleep

def fibo_gen(maximo = None):
    a, b  = 0, 1
    while not maximo or maximo >= a:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    fibo = fibo_gen(50)
    for element in fibo:
        print(element)
        sleep(1)
