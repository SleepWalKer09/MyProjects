"""
Un closure debe obedecer 3 reglas
1. Debe tener una funcion anidada
2. La funcion anidada debe referenciar un valor de un scope superior
3. La funcion que envuelve la nested debe retornarla tambien
"""

# Ejemplo de uso de closures en python

def multipicador(x):

    def multi(n):
        return x*n
    
    return multi

times10 = multipicador(10)
times4 = multipicador(4)

print(times10(3))
print(times10(5))
print(times10(times4(2)))