#Union set (junta todos los elementos excepto los que esten repetidos)
set1 = {3,4,5}
set2 = {5,6,7}

set3 = set1 | set2
print("Union de sets: ", set3)

#interseccion set (solo los elementos que esten repetidos)
set4 = {3,4,5}
set5 = {5,6,7}

set6 = set4 & set5
print("Interseccion de sets: ", set6)

#diferencia de sets (elimina todos los elementos en B que esten en A o viceversa)
set7 = {3,4,5}
set8 = {5,6,7}

set9 = set7 - set8
print("Diferencia sets (a-b): ", set9)
set10 = set8 - set7
print("Diferencia sets (b-a) ", set10)

#diferenca simetrica = contrario a interseccion, solo se quedan los elementos que no se compartan entre ambos sets
set11 = {3,4,5}
set12 = {5,6,7}

set13 = set11 ^ set12
print("Diferencia simetrica: ", set13)
