# Leer un archivo de texto en formato CSV (Valores Separados por espacios).

import csv

nombre_archivo = r'C:\Users\dsanz\Desktop\Codigos\Temario_Programacion2\Archivos_Modularidad\airbnb\airbnb.csv'

# Abrimos el archivo
with open(nombre_archivo, newline='', encoding='utf-8') as f:
    # Usamos csv.reader con el delimitador adecuado
    datos = csv.reader(f, delimiter='\t')
    
    # Extraemos los nombres de las columnas
    columnas = next(datos)  # La primera fila son los nombres de las columnas
    seleccion = ['id', 'host_id', 'neighbourhood_group_cleansed', 'accommodates', 'price']
    
    # Diccionario para traducir nombres de columnas
    traduccion = {
        'id': 'id',
        'host_id': 'anfitrion',
        'neighbourhood_group_cleansed': 'distrito',
        'accommodates': 'plazas',
        'price': 'precio'
    }
    
    # Lista para alojar los resultados
    alojamientos = []
    
    # Procesamos las filas del archivo
    for fila in datos:
        alojamiento = {}
        for i, valor in enumerate(fila):
            # Solo guardamos los valores de las columnas seleccionadas
            if columnas[i] in seleccion:
                alojamiento[traduccion[columnas[i]]] = valor
        alojamientos.append(alojamiento)

# Imprimimos los resultados
print(alojamientos)

def alojamientos_distritos(alojamientos):
    '''
    Función que devuelve un diccionario con el número de alojamientos en cada distrito.

    Parámetros:
    - alojamientos: Es una lista de diccionarios, donde cada diccionario contiene los datos de un alojamiento.
    
    Devuelve: Un diccionario con el número de alojamientos por distrito. 
    '''

    # Creamos el diccionario
    alojamiento_distritos = {}
    # Recorremos la lista de alojamientos
    for alojamiento in alojamientos:
        # Si el distrito ya aparece como clave del diccionario, incrementamos su valor en uno
        if alojamiento['distrito'] in alojamiento_distritos.keys():
            alojamiento_distritos[alojamiento['distrito']] += 1
        # Si el distrito no aparece como clave del diccionario, lo añadimos con valor 1.
        else:
            alojamiento_distritos[alojamiento['distrito']] = 1
    return alojamiento_distritos

# Ejemplo
print(alojamientos_distritos(alojamientos))