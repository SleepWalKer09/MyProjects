"""
Hacer un closure que:
    Retorne una funcion que retorna la division de un numero x entre un numero n
"""

def divisiones(n):
    def divisor(x):
        return (x/n)
    return divisor

def run():
    division3 = divisiones(3)
    print(division3(18)) #el resultado debe ser 6

    division5 = divisiones(5)
    print(division5(100)) #el resultado debe ser 20

    division10 = divisiones(18)
    print(division10(54)) #el resultado debe ser 3
    
if __name__ == '__main__':
    run()