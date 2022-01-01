# Hola 3 -> HolaHolaHola

def repeticiones(n):#Funcion envolvente
    def repetidor(string):#funcion anidada
        assert type(string) == str, "Solo se pueden utilizar strings" #afirmamos que el valor ingresado es un entero, de lo contrario envia el mensaje de error
        return(string*n)# llama a scope superior
    return repetidor #regresa la funcion anidada

def run():
    repetir5 = repeticiones(5)
    print(repetir5("Hola"))
    repetir10 = repeticiones(10)
    print(repetir5("Chris"))

if __name__ == '__main__':
    run()