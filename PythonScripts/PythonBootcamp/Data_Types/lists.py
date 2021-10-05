#lista de acciones con listas
dir(list)

x = ['red','blue','green','yellow','black',3,2.4]
print(type(x))

print(x[2])
print(x[-1])
len(x)

#pop = eliminar registro de lista, si vacio se elimina el ultimo registro
x.pop()
print(x)

#append = agrega a la lista
x.append(9)
print(x)

x.remove("yellow")
print(x)

#borrar lista
del x
print(x)
