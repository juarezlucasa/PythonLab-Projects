"""
 Cree un programa que utilizando una función, solicite la edad de la persona e
 imprima todos los años que la persona ha cumplido según el siguiente formato de ejemplo. 

1, 2, 3, 4, 5
Y 
5, 4, 3, 2, 1

"""

edad = int(input("Ingrese la edad del humano: "))
lista = []
for i in range(1, edad + 1):
    lista.append(i)

print(lista)

lista = []
while edad != 0:
    lista.append(edad)
    edad = edad - 1

print(lista)
