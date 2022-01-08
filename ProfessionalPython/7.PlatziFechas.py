"""
Tabla de formato de fechas en python

% y = year
% m = month
% d = day
% H = hour
% M = minute
% S = second

"""

from datetime import datetime
#  datetime.utcnow() --> para usar la hora universal

mytime = datetime.now()
print(f'hora del equipo: {mytime}')
print("")

myday = datetime.date.today()
print(f'Año: {myday.year}')
print(f'Mes: {myday.month}')
print(f'Dia: {myday.day}')


#cambio de formateo de fecha en python
my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')

#Formato 12 hrs
my_datetime = datetime.now()
print(my_datetime.strftime('%H:%M %P'))