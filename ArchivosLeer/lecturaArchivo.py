# Leer un archivo de texto en formato CSV (Valores Separados por Comas).

import csv

nombre_archivo = 'C:/archivos24/covid.csv'

with open(nombre_archivo, newline='', encoding='utf-8') as f:
    datos = csv.reader(f, delimiter=',', quotechar=';')

    for r in datos:
        print(r)
