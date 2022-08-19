"""
Suponga que tiene una verdulería y carga la cantidad
y el precio de lo comprado por un cliente.
Realice un programa que tome de a uno la cantidad
y el precio comprado por el cliente y al finalizar
la compra retorne el monto total gastado. 
"""

respuesta = True
importe_total = 0
while respuesta:
    producto = str(input("Ingrese nombre del producto: "))
    cantidad = int(input("Ingrese la cantidad comprada: "))
    importe = int(input("Ingrese monto de la compra: "))

    print(f"Producto: {producto} Cantidad: {cantidad} Importe: {importe}")

    importe_total = importe_total + importe
    if input("Desea ingresar otro producto? SI/NO: ") != "SI":
        respuesta = False

print("Importe total de la compra: ${0}".format(importe_total))
