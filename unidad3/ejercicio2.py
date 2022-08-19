"""
Escriba un programa que consulte al usuario por una oración
y comente al usuario cuantas veces aparece la letra “a”. 
"""

oracion = input("Escriba a continuación una oracion: \n")
cont = 0
for x in oracion:
    if x == "a":
        cont += 1

print("La letra 'a' aparece {0} veces".format(cont))
