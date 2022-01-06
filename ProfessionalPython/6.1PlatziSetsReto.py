"""
Teniendo dos sets, aplicar las operaciones de sets
"""
set1 = {'🍎', '🍊', '🍇', '🍓', '🍈'}
set2 = {'🍉', '🍊', '🍒', '🍓', '🍋'}

#Union

set3 = set1.union(set2)
print("Union de sets: ", set3)
print("")
#interseccion
set4 = set1.intersection(set2)
print("Interseccion de sets: ", set4)
print("")
#diferencia de sets
set5 = set1.difference(set2)
print("Diferencia sets (a-b): ", set5)
print("")
set6 = set2.difference(set1)
print("Diferencia sets (b-a) ", set6)
print("")

#diferenca simetrica
set7 = set1.symmetric_difference(set2)
print("Diferencia simetrica: ", set7)
print("")
