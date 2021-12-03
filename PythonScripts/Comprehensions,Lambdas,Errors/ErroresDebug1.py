#El siguiente codigo tiene errores de logica, se utiliza la herramienta debugging para corregirlo

def divisor(num):
    divisors = []
    for i in range(1, num+1):
        #correccion, el resultado del modulo debe ser 0
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un numero: "))
    print(divisor(num))
    print("Termino el programa")

if __name__ == '__main__':
    run()