import pandas as pd
import numpy as np

d1 = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": (10031414),
    "hobbies": ["basquetbol", "tenis", "futbol"]
}

print(d1)

d3 = dict(Nombre= 'Sara',
          Edad = 27,
          Documento= (129129),
          Hobbie= ['Futbol', 'natacion']
          )

print(d3)

print("===================================")

print(d1["Nombre"])
print(d1.get('Nombre'))
print(d1["Documento"])
d1["Nombre"] = "Laura"
print(d1["Nombre"])

d1["Direccion"] = "Calle123"
print(d1["Direccion"])

print("===================================")
#Recorriendo el diccionario

for x in d1:
    print(d1[x])

#Otra forma
for x, y in d1.items():
    print(x, y)

#Anidando diccionarios

anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}

d = {"anidado1": anidado1,
     "anidado2": anidado2,
     }

d.clear()

print(d)

d = {'a': 1, 'b': 2}
it = d.items()
print(it)
print(list(it))
print(list(it)[0][0])

k = d.keys()
print(k)
print(list(k))

v = d.values()
print(v)
print(list(v))

d.pop('a')
print(d)

d.popitem() #elimina el ultimo registro del dicc: 
print(d)

d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'b': 400}

d1.update(d2)
print(d1)
