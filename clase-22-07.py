
# Online Python - IDE, Editor, Compiler, Interpreter
tupla = ((1, 2, "hola"), ("segunda", "tupla"))
t = (("a", 11), ("a", 10), ("b", 1), ("c", 22)) #tupla dentro de tupla

tupla_datos_personales = ["Santiago", "Hernandez", tuple("16 de junio 2002"), tuple("Bogota"), "cedula", 1007530123]
print(tupla_datos_personales)

tupla_datos_personales[0] = "Enrique"
print(tupla_datos_personales)

lista = [1, 2, 3, 4, 5]
print(lista[0:2]) #Slicing
for t in tupla_datos_personales:
    print(t)