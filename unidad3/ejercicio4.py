"""
Escriba un programa que solicite la edad de la persona
e imprima todos los años que la persona ha cumplido. 
"""

edad = int(input("Ingrese la edad de la persona \n"))

for i in range(edad):
    print("La persona cumplio {0} años".format(i + 1))
