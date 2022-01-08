from datetime import date, datetime
import pytz
"""
BD con zonas horarias del mundo:
https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes
"""

# TZ de mexico, colomba y venezuela

bogotaTZ = pytz.timezone("America/Bogota")
bogota_fecha = datetime.now(bogotaTZ)
print("Bogota: ", bogota_fecha.strftime("%d/%m/%Y, %H:%M:%S"))

mexicoTZ = pytz.timezone("America/Mexico_City")
mexico_fecha = datetime.now(mexicoTZ)
print("CDMX: ", mexico_fecha.strftime("%d/%m/%Y, %H:%M:%S"))

caracasTZ = pytz.timezone("America/Caracas")
caracas_fecha = datetime.now(caracasTZ)
print("Caracas: ", caracas_fecha.strftime("%d/%m/%Y, %H:%M:%S"))