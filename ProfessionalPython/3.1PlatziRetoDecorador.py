# Decorador que verifica el tiempo de ejecucion de funciones y lo imprime una pantalla

from datetime import date, datetime

def execution_time(func):
# *        == operador de desestructuracion de python
# *args    == no importa la cantidad de argumentos posicionales que se envien, la funcion los va a recibir
# **kwargs == no importa la cantidad de argumentos nombrados, la funcion los va a recibir
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)#ejecuta la funcion
        final_time = datetime.now()
        time_lapse = final_time - initial_time
        print("Pasaron " + str(time_lapse.total_seconds()) + " Segundos")
    return wrapper

#ver cuanto se tarda esta funcion en ejecutarse un millon de veces
@execution_time
def random_func():
    # _ -- ciclo for donde no nos interesa el valor que estemos iterando, se pone un guion bajo 
    for _ in range(1,1000000):
        pass

@execution_time
def suma(a:int,b:int) ->int:
    return a+b


@execution_time
def saludo(nombre=' Luis '): #parametro nombrado (kwargs)
    print('Hola ' + nombre)

random_func()
suma(5,5)
saludo("Chris")