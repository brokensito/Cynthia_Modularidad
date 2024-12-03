
from procesador import procesar_alojamientos
from estadisticas import alojamientos_distritos
from barato import alojamientos_baratos
# Ruta al archivo CSV
nombre_archivo = 'C:/archivos24/ArchivosLeer/proyecto2/airbnb.csv'

# Procesar los alojamientos
alojamientos = procesar_alojamientos(nombre_archivo)

# Calcular estadísticas de distritos
estadisticas = alojamientos_distritos(alojamientos)

# Imprimir resultados
print("Estadísticas por distrito:")
print(estadisticas)

# Calcular los alojamientos más baratos en un distrito específico
distrito = 'Arganzuela'  # Puedes cambiar esto por cualquier distrito
n = 10  # Número de alojamientos baratos a buscar

baratos = alojamientos_baratos(alojamientos, distrito, n)  # Esta función debe estar definida previamente

# Encabezado
print(f"Top {n} alojamientos más baratos en {distrito}:")
print("{:<10} {:<15} {:<20} {:<10} {:<10}".format("ID", "Anfitrión", "Distrito", "Plazas", "Precio"))
print("-" * 65)

# Datos
for alojamiento in baratos:
    print("{:<10} {:<15} {:<20} {:<10} {:<10}".format(
        alojamiento.get('id', ''),
        alojamiento.get('anfitrion', ''),
        alojamiento.get('distrito', ''),
        alojamiento.get('plazas', ''),
        alojamiento.get('precio', '')
    ))



