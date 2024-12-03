#  Leer un archivo CSV sobre una estructura de datos tipo diccionario.

import csv

nombre_archivo = r'C:\Users\dsanz\Desktop\Codigos\Temario_Programacion2\ArchivosLeer\ArchivosLeer\covid100.csv'



with open(nombre_archivo, newline='', encoding='utf-8') as f:
    covid_19_colombia = csv.DictReader(f)

    for r in covid_19_colombia:
        print(r)
