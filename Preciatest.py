import pandas as pd
import logging

# Configurar el sistema de logging para el punto extra :D
logging.basicConfig(level=logging.INFO)

# 1. Leer csv y generar un data frame con los datos del fichero
archivo_csv = 'titanic.csv'
df = pd.read_csv(archivo_csv)

# 2. Mostrar info general del dataframe.
logging.info("Dimensiones del DataFrame: %s", df.shape)
logging.info("Número de datos que contiene: %s", df.size)
logging.info("Nombres de columnas: %s", df.columns)
logging.info("Nombres de filas: %s", df.index)
logging.info("Tipos de datos de las columnas:\n%s", df.dtypes)
logging.info("Primeras 10 filas:\n%s", df.head(10))
logging.info("Últimas 10 filas:\n%s", df.tail(10))

# 3. Mostrar los datos del pasajero 148
logging.info("Datos del pasajero con identificador 148:\n%s", df.loc[147])

# 4. Mostrar las filas pares del DataFrame.
logging.info("Filas pares:\n%s", df.iloc[::2])

# 5. Mostrar personas en primera clase ordenadas alfabéticamente.
nombres_primera_clase = df[df['Pclass'] == 1]['Name'].sort_values()
logging.info("Nombres en primera clase ordenados alfabéticamente:\n%s", nombres_primera_clase)

# 6. Mostrar porcentaje de personas que sobrevivieron y murieron.
porcentaje_muertos = df['Survived'].value_counts(normalize=True).get(0, 0) * 100
logging.info("Porcentaje de personas que murieron: %s", int(porcentaje_muertos))

porcentaje_vivos = df['Survived'].value_counts(normalize=True).get(1, 0) * 100
logging.info("Porcentaje de personas que vivieron: %s", int(porcentaje_vivos))

# 7. Mostrar porcentaje de personas que sobrevivieron en cada clase.
porcentaje_sobrevivientes_clase = df.groupby('Pclass')['Survived'].mean() * 100
logging.info("Porcentaje de personas que sobrevivieron en cada clase:\n%s", porcentaje_sobrevivientes_clase)

# 8. Eliminar pasajeros con edad desconocida.
df_sin_edad_desconocida = df.dropna(subset=['Age'])

# 9. Mostrar edad media de mujeres en cada clase.
edad_media_mujeres_por_clase = df[df['Sex'] == 'female'].groupby('Pclass')['Age'].mean()
logging.info("Edad media de mujeres en cada clase:\n%s", edad_media_mujeres_por_clase)

# 10. Añadir columna booleana para indicar si el pasajero es menor de edad.
df['Menor_de_edad'] = df['Age'] < 18

# 11. Mostrar porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
porcentaje_sobrevivientes_menores = df[df['Menor_de_edad']]['Survived'].mean() * 100
porcentaje_sobrevivientes_mayores = df[~df['Menor_de_edad']]['Survived'].mean() * 100
logging.info("Porcentaje de menores que sobrevivieron: %s", porcentaje_sobrevivientes_menores)
logging.info("Porcentaje de mayores que sobrevivieron: %s", porcentaje_sobrevivientes_mayores)
