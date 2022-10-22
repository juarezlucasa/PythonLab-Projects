"""
Tome el ejercicio de cálculo de números pares e impares de la unidad 2 
y agréguele un bucle al código de forma de simplificarlo. 
"""

import sys


def esmultiplodedos(numero):
    resultado = numero % 2
    if resultado == 0:
        print("El numero ", numero, " es multiplo de 2")
    else:
        print("El numero ", numero, " NO es multiplo de 2")


# Genero una lista con los valores que llegan por parametros
lista = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

for i in lista:
    esmultiplodedos(i)
