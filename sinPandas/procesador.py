import csv

def procesar_alojamientos(nombre_archivo):
    '''
    Procesa un archivo CSV de alojamientos y devuelve una lista de diccionarios con los datos seleccionados.

    Parámetros:
    - nombre_archivo: Ruta del archivo CSV.

    Devuelve:
    - Una lista de diccionarios, cada uno representando un alojamiento.
    '''
    with open(nombre_archivo, newline = '', encoding='utf-8') as f:
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
    
    return alojamientos
