import matplotlib.pyplot as plt

def sectores_tipos_alojamientos(alojamientos, distritos):
    '''
    Función que dibuja un diagrama de sectores con los porcentajes de tipos de alojamientos en unos distritos dados.

    Parámetros:
    - alojamientos: Es una lista de diccionarios, donde cada diccionario contiene los datos de un alojamiento.
    - distritos: Es una lista con los nombres de los distritos. 
    '''
    # Definimos la figura y los ejes del gráfico
    fig, ax = plt.subplots()
    # Filtramos los distritos de la lista de distritos dada, después contamos la frecuencias de los tipos de alojamientos y dibujamos el diagrama de sectores
    alojamientos[alojamientos.distrito.isin(distritos)].tipo_alojamiento.value_counts(normalize = True).plot(kind = 'pie',  autopct='%1.0f%%', ax = ax)
   
    # Ponermos el título
    ax.set_title('Distribución del porcentaje de tipos de alojamientos\n Distritos de ' + ', '.join(distritos), loc = "center", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
    # Eliminamos la etiqueta del eje y
    ax.set_ylabel('')
    # Guardamos el gráfico.
    plt.show()
    return sectores_tipos_alojamientos

