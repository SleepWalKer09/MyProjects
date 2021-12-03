def divisor(num):
    divisors = []
    for i in range(1, num+1):
        if (num % i == 0):
            divisors.append(i)
    return divisors

def run():
    while True:
        #intenta imprimir los divisores si el valor ingresado es un numero
        try:
            num = int(input("Ingresa un numero: "))
            if num < 0:
                raise ValueError
            print(divisor(num))
            print("Termino el programa")
            break
        except ValueError:
            print("Debes ingresar un numero entero positivo")

if __name__ == '__main__':
    run()
