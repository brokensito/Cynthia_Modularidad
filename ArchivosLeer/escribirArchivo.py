# Escribir contenido a un archivo de texto plano con la función write().

nombre_archivo = 'C:/archivos24/ciudades.txt'

with open(nombre_archivo, 'w', encoding='utf-8') as f:
    while True:
        ciudad = input('Escriba un nombre de ciudad (OK para finalizar el ingreso de datos): ')

        if ciudad != 'OK':
            f.write(ciudad)
            f.write('\n')
        else:
            break
    
    print('Ha finalizado la escritura del archivo.')
