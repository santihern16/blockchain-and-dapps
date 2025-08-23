import pandas as pd

# Lista
lista = []

# Diccionario
diccionario = {}

# Tupla (se crea nueva cada vez, ya que es inmutable)
tupla = ()

# DataFrame
df = pd.DataFrame(columns=["col1", "col2"])

while True:
    print("\nElige estructura:")
    print("1. Lista")
    print("2. Diccionario")
    print("3. Tupla")
    print("4. DataFrame")
    print("5. Salir")
    op = input("Opción: ")

    if op == "1":
        print("\nLista CRUD:")
        print("a. Crear (agregar)")
        print("b. Leer (mostrar)")
        print("c. Actualizar (modificar)")
        print("d. Eliminar (borrar)")
        acc = input("Acción: ")
        if acc == "a":
            valor = input("Valor a agregar: ")
            lista.append(valor)
        elif acc == "b":
            print(lista)
        elif acc == "c":
            idx = int(input("Índice a modificar: "))
            valor = input("Nuevo valor: ")
            lista[idx] = valor
        elif acc == "d":
            idx = int(input("Índice a borrar: "))
            del lista[idx]

    elif op == "2":
        print("\nDiccionario CRUD:")
        print("a. Crear (agregar)")
        print("b. Leer (mostrar)")
        print("c. Actualizar (modificar)")
        print("d. Eliminar (borrar)")
        acc = input("Acción: ")
        if acc == "a":
            clave = input("Clave: ")
            valor = input("Valor: ")
            diccionario[clave] = valor
        elif acc == "b":
            print(diccionario)
        elif acc == "c":
            clave = input("Clave a modificar: ")
            valor = input("Nuevo valor: ")
            diccionario[clave] = valor
        elif acc == "d":
            clave = input("Clave a borrar: ")
            del diccionario[clave]

    elif op == "3":
        print("\nTupla CRUD:")
        print("a. Crear (nueva tupla)")
        print("b. Leer (mostrar)")
        acc = input("Acción: ")
        if acc == "a":
            valores = input("Valores separados por coma: ")
            tupla = tuple(valores.split(","))
        elif acc == "b":
            print(tupla)

    elif op == "4":
        print("\nDataFrame CRUD:")
        print("a. Crear (agregar fila)")
        print("b. Leer (mostrar)")
        print("c. Actualizar (modificar fila)")
        print("d. Eliminar (borrar fila)")
        acc = input("Acción: ")
        if acc == "a":
            v1 = input("Valor col1: ")
            v2 = input("Valor col2: ")
            df.loc[len(df)] = [v1, v2]
        elif acc == "b":
            print(df)
        elif acc == "c":
            idx = int(input("Índice de fila a modificar: "))
            v1 = input("Nuevo valor col1: ")
            v2 = input("Nuevo valor col2: ")
            df.loc[idx] = [v1, v2]
        elif acc == "d":
            idx = int(input("Índice de fila a borrar: "))
            df = df.drop(idx).reset_index(drop=True)

    elif op == "5":
        break