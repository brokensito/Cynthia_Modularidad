import pandas as pd

# Leer el archivo Excel y convertirlo a listas
info = 'C:/archivos24/info.xlsx'

try:
    # Leer datos existentes y convertirlos a listas
    file = pd.read_excel(info)
    nombres = file['Nombre'].tolist()
    apellidos = file['Apellido'].tolist()
    telefonos = file['Telefono'].tolist()
except FileNotFoundError:
    # Si el archivo no existe, inicializar listas vacías
    print("Archivo no encontrado. Creando un archivo nuevo...")
    nombres, apellidos, telefonos = [], [], []

salir = True

while salir:
    print("\n1- Mostrar datos")
    print("2- Insertar datos")
    print("3- Salir")
    x = int(input("\nSelecciona una opción: "))

    if x == 1:
        # Mostrar los datos almacenados
        print("\nDatos almacenados:")
        for i in range(len(nombres)):
            print(f"{nombres[i]} {apellidos[i]} - {telefonos[i]}")

    elif x == 2:
        # Insertar datos
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        tel = input("Teléfono: ")

        # Agregar los datos a las listas
        nombres.append(nom)
        apellidos.append(ape)
        telefonos.append(tel)
        print("Datos añadidos correctamente.")

        # Convertir las listas a un DataFrame y guardar en Excel
        data = {'Nombre': nombres, 'Apellido': apellidos, 'Telefono': telefonos}
        df = pd.DataFrame(data)
        df.to_excel(info, index=False)
        print("Datos guardados en el archivo Excel.")

    elif x == 3:
        salir = False
        print("Saliendo del programa.")

    else:
        print("\nSelecciona una opción válida.")

        
 