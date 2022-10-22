"""
Tome dos valores por consola, y guarde en una lista:
[primer_valor, segundo_valor, la_suma_de_los_valores]
Presente el resultado en la terminal del editor
"""

primer_valor = int(input("Ingrese el primer valor: "))
segundo_valor = int(input("Ingrese el segundo valor: "))

lista = []

lista.append(primer_valor)
lista.append(segundo_valor)
lista.append(primer_valor + segundo_valor)

print(lista)
