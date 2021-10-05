#[] listas
#() tuplas
#{} diccionarios

x = {"number":"1", "name": "blue", "age": 200}
print(x)

#acceder dict
print(x["age"])
print(x["name"])
print(x["number"])
len(x)

#agrega al diccionario, se tiene que meter la key y su valor
x["year"] = 2021
print(x)

#pop = elimina registro seleccionado
x.pop("age")
print(x)

#popitem = elimina el ultimo registro del dict
x.popitem()
print(x)
