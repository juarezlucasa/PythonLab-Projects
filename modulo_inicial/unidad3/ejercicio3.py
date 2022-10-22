"""
Escriba un programa que consulte al usuario por una oración
y comente al usuario cuantas veces aparecen todas las vocales
considerando minúsculas, mayúsculas y acentos.  
"""


def contvocales(x):
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    cont_vocales = 0
    for i in vocales:
        if str.lower(x) == i:
            cont_vocales += 1
    return cont_vocales


oracion = input("Escriba a continuación una oracion: \n")
cont = 0
for x in oracion:
    cont = cont + contvocales(x)

print("En la oracion, aparecen ", cont, "vocales")
