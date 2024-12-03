import pandas as pd
import os
print(os.getcwd())

# Leer archivo CSV
df_csv = pd.read_csv('archivo.csv')
print("Datos del CSV:")
print(df_csv.head())

# Leer archivo Excel
df_excel = pd.read_excel('archivo.xlsx')
print("\nDatos del Excel:")
print(df_excel.head())

# Realizar alguna modificación (ejemplo: agregar una nueva columna)
df_csv['Nueva Columna'] = 'Valor Ejemplo'

# Guardar la modificación en un nuevo archivo CSV
df_csv.to_csv('archivo_modificado.csv', index=False)

# Guardar el DataFrame en un archivo Excel
df_excel.to_excel('archivo_modificado.xlsx', index=False)

print("\nArchivos guardados correctamente.")
