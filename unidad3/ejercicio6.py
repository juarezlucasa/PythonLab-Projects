"""
A partir del ejercicio 5 cree un programa que
vaya agregando en una lista las compras realizadas.
"""
import pprint

lista = []
respuesta = True
while respuesta:
    producto = str(input("Ingrese nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    importe = int(input("Ingrese monto de la compra: "))
    # Armo una tupla con los valores, y la inserto en una lista.
    tupla = (producto, cantidad, importe)
    lista.append(tupla)

    if input("Desea ingresar otro producto? SI/NO: ") != "SI":
        respuesta = False

pprint.pprint(lista)
importe_total = 0
# Recorro la lista, me quedo con la posición del importe y acumulo en importe_total
for i in lista:
    importe_total = importe_total + i[2]

print("Importe total de la compra: ${0}".format(importe_total))
