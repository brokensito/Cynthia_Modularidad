import matplotlib.pyplot as plt
# Procesar alojamientos desde el CSV
from procesador import procesar_alojamientos
nombre_archivo = '/Users/david/Documents/Codigos Programacion/Temario_Programacion2/sinPandas/airbnb.csv'
alojamientos = procesar_alojamientos(nombre_archivo)

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



def graficar_alojamientos_por_distrito(diccionario_distritos):
    '''
    Función que genera una gráfica de barras a partir de un diccionario con el número de alojamientos por distrito.

    Parámetros:
    - diccionario_distritos: Un diccionario donde las claves son los distritos y los valores son el número de alojamientos.
    '''
    # Extraemos los datos del diccionario
    distritos = list(diccionario_distritos.keys())
    cantidades = list(diccionario_distritos.values())

    # Crear la figura y el eje
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Crear la gráfica de barras
    ax.bar(distritos, cantidades, color='skyblue', edgecolor='black')
    
    # Configurar título y etiquetas
    ax.set_title('Número de alojamientos por distrito', fontsize=16, fontweight='bold')
    ax.set_xlabel('Distritos', fontsize=12)
    ax.set_ylabel('Número de alojamientos', fontsize=12)
    ax.set_xticks(range(len(distritos)))
    ax.set_xticklabels(distritos, rotation=45, ha='right', fontsize=10)

    # Mostrar la gráfica
    plt.tight_layout()
    plt.show()

# Ejemplo de uso:
# Suponiendo que ya tienes el DataFrame o lista de alojamientos procesados
# y la función alojamientos_distritos definida.

# Obtener los datos reales
resultado = alojamientos_distritos(alojamientos)

# Graficar los resultados reales
graficar_alojamientos_por_distrito(resultado)


