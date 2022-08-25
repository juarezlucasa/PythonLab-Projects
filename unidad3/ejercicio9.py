"""
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios
Respuesta: Considero mas facil guardar la información en diccionarios, dado que simplifica mucho la consulta,
Nos ahorramos de tener que escribir un for que recorra toda una lista en busca del file, simplemente lo buscamos pasandole
la key como argumento. Me parece mucho mas práctico, y creo que tambien mas performante.
"""
import pprint


def alta(producto, cantidad, importe, diccionario):
    diccionario[producto] = {
        "Cantidad": cantidad,
        "Importe": importe,
    }
    pprint.pprint(diccionario)
    print("Producto ingresado con éxito")
    return diccionario


def baja(producto, diccionario):
    del diccionario[producto]
    pprint.pprint(diccionario)
    return diccionario


def consulta(producto, diccionario):
    pprint.pprint(diccionario.get(producto))


def modificar(producto, cantidad_modif, importe_modif, diccionario):

    diccionario[producto] = {"Cantidad": cantidad_modif, "Importe": importe_modif}
    pprint.pprint(diccionario)


diccionario = {}
# Genero un menu para entrar en cada una de las funciones.
print("---" * 50)
print("Menu del programa \n")
print("1 - Alta de producto")
print("2 - Baja de producto")
print("3 - Consulta de producto")
print("4 - Modificacion de producto")
print("9 - Salir \n")
opcion = int(input("ELIGE UNA OPCION: "))
print("---" * 50)

while opcion != 9:
    if opcion == 1:
        producto = str(input("Ingrese nombre del producto: "))
        cantidad = int(input("Ingrese cantidad adquirida: "))
        importe = int(input("Ingrese importe por el total adquirido del producto: "))
        diccionario = alta(producto, cantidad, importe, diccionario)
    if opcion == 2:
        producto = str(input("Ingrese nombre del producto a eliminar: "))
        diccionario = baja(producto, diccionario)
    if opcion == 3:
        producto = str(input("Ingrese nombre del producto a consultar: "))
        indice = consulta(producto, diccionario)
    if opcion == 4:
        producto = str(input("Ingrese nombre del producto a modificar: "))
        cantidad_modif = str(input("Ingrese nueva cantidad: "))
        importe_modif = str(input("Ingrese nuevo importe: "))
        modificar(producto, cantidad_modif, importe_modif, diccionario)
    if opcion == 9:
        break
    print("---" * 50)
    opcion = int(input("ELIGE UNA OPCION: "))
