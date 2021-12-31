"""
Ejericio de palabras palindromas usando tipado estatico en python

Crear ambiente virtual: py -m venv venv
Entrar ambiente virtual: .\venv\Scripts\activate

Usar mypy para encontrar errores de tipado: mypy + NombreArchivo + --check-untyped-defs
"""

#funcion donde entra un string y regresa un booleano
def is_palindrome(string: str) -> bool:
    string = string.replace(" ","".lower())
    #string sera igual al string al reves
    return string == string[::-1] # [::-1] --- Da vuelta al iterable

def run():
    print(is_palindrome("ana"))

if __name__ == '__main__':
    run()