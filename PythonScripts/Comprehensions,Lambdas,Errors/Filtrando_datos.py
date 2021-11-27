DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    #de todos los trabajadores guadaremos el nombre del empleado siempre y cuando el lenguaje que domine sea python
    python_devs = [worker["name"] for worker in DATA if worker["language"]== "python"]
    #usando list comprehension mostrar solo el nombre de los empleados que trabajen en platzi
    platzi_worker = [worker["name"] for worker in DATA if worker["organization"]== "platzi"]
    #uso de high order filter function
    adults = list(filter(lambda worker: worker["age"]>18, DATA))
    #uso de funcion map para que la funcion filter no traiga todos los registros
    adults = list(map(lambda worker: worker["name"], adults))# sobreescribir adults para que solo traiga el nombre del empleado mientras la funcion filter se cumpla

    #crear diccionarios con llaves extras (all -> true o false) que sepa cuando alguien ya es anciano
    # Transformar todos los diccionarios en DATA en un diccionario nuevo que es la combinacion de los originales con el diccionario "old" y su valor que es el resultado de la expresion age>70
    # | = unir diccionario con otro diccionario (solo a partir de python 3.9)--> SUMAR DICCIONARIOS con |
    old = list(map(lambda worker: worker | {"old": worker["age"]>70},DATA ))

    for worker in adults:
        print(worker)

if __name__ == '__main__': 
    run() 