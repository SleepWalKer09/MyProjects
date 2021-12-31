"""
Reto1: Verificacion de un numero primo usando tipado estatico
"""

def primo(numero:int) -> bool:
    resultado = [i for i in range(1,numero+1) if numero%i==0]
    return len(resultado)==2

def run():
    print(primo(17))

if __name__ == '__main__':
    run()