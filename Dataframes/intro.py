import pandas as pd
import numpy as np

df = pd.DataFrame()
print(df)

data = np.array([['','Col1','Col2'],
                ['Row1', 1, 2],
                ['Row2',3, 4]])

print(data)

print("============================")

print(pd.DataFrame(data=data[1:,1:],
                  index=data[1:, 0],
                  columns=data[0,1:]))

df = pd.DataFrame(np.array([[1,2,3],[4,5,6]]), columns=["col1", "col2", "col3"], index=["row1", "row2"])

print(df)
print(df.shape) # tamaño del df, (filas, cols)
print(len(df)) # 2 - cantidad de filas

print("============================")

df = pd.DataFrame({"A":[1,2,6],
                   "B":[3, 5, 7],
                   "C":[4, 6, 2]}, index=["Row1", "Row2", "Row3"])

#df.index =["Row1", "Row2", "Row3"]
print(df)

print("============================")

print("Trae el valor de la posicion [0, 0]: ", df.iloc[0, 0]) # primera fila
print(df.iloc[0]["A"]) # primera fila, columna A
print("flag",df.iloc[0]) # primera fila completa
print(df.at["Row1", "A"]) # primera fila, columna A usando el nombre del indice
print(df.iat[0, 0]) # primera fila, columna A usando la posicion

print("============================")

print(df.loc[:, "A"]) # todas las filas, columna A

df.set_index("A", inplace=True) # cambia el indice a la columna A
print(df)

data = np.array([
    ["Juan", "Perez", "Maria", "Gomez"],
    ["Ana", "Lopez", "Luis", "Martinez"],
    ["Carlos", "Sanchez", "Lucia", "Diaz"]
])

df_names = pd.DataFrame(data, columns=["Nombre1", "Apellido1", "Nombre2", "Apellido2"])
print(df_names)