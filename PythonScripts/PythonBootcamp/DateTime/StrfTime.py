import datetime

x = datetime.datetime.now()

#formato de mes
print(x.strftime("%B"))
# formato de dia
print(x.strftime("%A"))
# dia de la semana (0 al 6)
print(x.strftime("%w"))
#formato local de fecha completa
print(x.strftime("%x"))