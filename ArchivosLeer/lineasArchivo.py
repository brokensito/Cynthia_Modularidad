# Leer e imprimir las n primeras líneas de un archivo de texto plano.

from itertools import islice

def leer_n_lineas_archivo(archivo, n=20):

    with open(archivo, 'r') as f:
        for l in islice(f, n):
            print(l, end='')

nombre_archivo = 'C:/archivos24/palabras_ingles.txt'
n = 50

leer_n_lineas_archivo(nombre_archivo, n)
