#  Imprimir el valor asociado a determinadas columnas de un archivo CSV.

import csv

ruta_archivo = 'C:/archivos24/covid100.csv'

with open(ruta_archivo, newline='', encoding='utf-8') as f:
    covid_colombia = csv.DictReader(f)

    for r in covid_colombia:
        print(r['ID de caso'], r['Fecha de notificación'], r['Ciudad de ubicación'], r['atención'])
