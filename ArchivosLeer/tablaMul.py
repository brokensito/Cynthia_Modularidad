# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:23:33 2022

@author: cynthya.garcia
"""
import os
# Solicitar un número al usuario
while True:
    try:
        n = int(input('Introduce un número entero entre 1 y 10: '))
        if 1 <= n <= 10:
            break
        else:
            print("Por favor, introduce un número entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")

# Generar el nombre del archivo
ruta_guardado = r'C:/archivos24/'  # Cambia esta ruta
os.makedirs(ruta_guardado, exist_ok=True)  # Crea el directorio si no existe

# Generar el nombre del archivo con la ruta completa
nombre_fichero = os.path.join(ruta_guardado, f'tabla-{n}.txt')

import os
print("Directorio actual:", os.getcwd())
# Abrir el archivo en modo escritura y generar la tabla de multiplicar
with open(nombre_fichero, 'w') as f:
    for i in range(1, 11):
        f.write(f'{n} x {i} = {n * i}\n')

print(f"Tabla de multiplicar guardada en el archivo: {nombre_fichero}")

