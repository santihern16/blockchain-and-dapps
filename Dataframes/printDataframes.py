import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.array([["Carlos", "Camilo", "Arango", "Rojas", 40, "Bogotá"],
                                 ["Segismundo", "", "Ruiz", "Lombardia", 18, "Cali"],
                                 ["Santiago", "Hernandez", "Gomez", "Doncel", 35, "Medellin"]]),
                  columns= ['Primer Nombre',
                            'Segundo Nombre',
                            'Primer Apellido',
                            'Segundo Apellido',
                            'Edad',
                            'Ciudad'])

print(df)
print("========================================")

print(df.head())
print("========================================")

print(df["Primer Nombre"])
print(df[["Primer Nombre","Primer Apellido"]])
print("========================================")

print(df[df["Primer Nombre"] == "Segismundo"])
print("========================================")

df.loc[df["Primer Nombre"] == "Segismundo", "Edad"] = 29
print(df)
print("========================================")

df = df.drop("Ciudad", axis=1)
print(df)
print("========================================")

df = df.drop(1)
print(df)
print("========================================")