
import csv
from leerair import *
from funAlojamientos import alojamientos_distritos
from procesador import procesar_alojamientos
# Ruta al archivo CSV
nombre_archivo = 'C:/archivos24/ArchivosLeer/proyecto2/airbnb.csv'

# Procesar los alojamientos
alojamientos = procesar_alojamientos(nombre_archivo)

# Calcular estadísticas de distritos
estadisticas = alojamientos_distritos(alojamientos)

# Imprimir resultados
print(estadisticas)
