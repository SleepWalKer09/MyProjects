#lectura y escrtura de archivos en python
# r -> read   --- lee los elementos del archivo
# w -> write  --- modifica el archivo, sobreescribiendo todo cada vez que se actualiza
# a -> append --- modifica el archivo, solo actualiza los cambios realizados lo demas se queda igual

def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f: #leer cada linea del archivo
            numbers.append(int(line))
    print(numbers)

def write():
    #cada vez que se ejecute este codigo, se reemplaza todo el archivo "names.txt"
    names = ["Chris", "Facundo", "Miguel", "Pepe","Rocío","Nicolas"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names:#por cada nombre en la lista se agregara el nombre al archivo
            f.write(name)
            f.write("\n")
    


def run():
    write()

if __name__ == '__main__':
    run()