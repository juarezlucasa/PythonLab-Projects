"""
A partir del ejercicio 5 cree un programa que vaya agregando en un
diccionario las compras realizadas.
"""

diccionario = {}
respuesta = True
while respuesta:
    producto = str(input("Ingrese nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    importe = int(input("Ingrese monto de la compra: "))
    # Armo un diccionario con estos valores
    diccionario[producto] = {
        "Cantidad": cantidad,
        "Importe": importe,
    }

    if input("Desea ingresar otro producto? SI/NO: ") != "SI":
        respuesta = False

importe_total = 0
for i in diccionario:
    importe_total = importe_total + diccionario[i].get("Importe")

print("Importe total de la compra: ${0}".format(importe_total))
