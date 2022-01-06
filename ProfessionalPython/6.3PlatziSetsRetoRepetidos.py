"""
Eliminar los duplicados usando sets
"""
# Al declarar el set como una lista y pedir que se regrese como set, python automaticamente borra los elementos duplicados sin necesidad de hacer lineas extra de codigo

def remove_duplicates(some_list):
    return list(set(some_list))


def run():
    some_list = [1,1,2,2,4]
    print(remove_duplicates(some_list))

if __name__ == '__main__':
    run()