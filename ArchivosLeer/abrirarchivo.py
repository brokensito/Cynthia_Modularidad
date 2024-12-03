# -*- coding: utf-8 -*-

#Abrir un archivo csv y escribir sobre él

import pandas as pd

# Ruta del archivo Excel
info = r'C:\Users\dsanz\Desktop\Codigos\Temario_Programacion2\ArchivosLeer\ArchivosLeer\info.xlsx'


# Leer el archivo Excel
file = pd.read_excel(info)

# Inicializar listas
salir = True

while salir:
    print("\n1- Mostrar datos")
    print("2- Insertar datos")
    print("3- Salir")
    x = int(input("\nSelecciona una opción: "))

    if x == 1:
        print(file)

    elif x == 2:
        # Solicitar los datos al usuario
        nom = input("Nombre: ")
        ape = input("Apellido: ")
        tel = input("Teléfono: ")

        # Crear una fila como lista
        nueva_fila = pd.DataFrame([[nom, ape, tel]], columns=['Nombre', 'Apellido', 'Telefono'])

        # Concatenar el DataFrame original con la nueva fila
        file = pd.concat([file, nueva_fila], ignore_index=True)

        # Guardar los cambios en el archivo Excel
        file.to_excel(info, index=False)

    elif x == 3:
        salir = False

    else:
        print("\nSelecciona una opción válida")
