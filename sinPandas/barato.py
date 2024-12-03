
def alojamientos_baratos(alojamientos, distrito, n):
    '''
    Función que devuelve una lista con los n alojamientos más baratos en un distrito dado.

    Parámetros: 
    - alojamientos: Es una lista de diccionarios, donde cada diccionario contiene los datos de un alojamiento.
    - distrito: Es una cadena con el nombre del distrito.
    - n: Es un entero con el número de alojamientos a devolver.

    Devuelve:
    - Una lista con los n alojamientos más baratos del distrito dado.
    '''
    # Filtramos los alojamientos del distrito
    alojamientos_distrito = [alojamiento for alojamiento in alojamientos if alojamiento['distrito'] == distrito]
    # Definimos una función de ordenación con la clave para la ordenación
    def orden(dict): return float(dict['precio'][1:])
    # Ordenamos la lista de alojamientos con la función de ordenación
    ranking_alojamientos = sorted(alojamientos_distrito, key=orden)
    return ranking_alojamientos[:n]
