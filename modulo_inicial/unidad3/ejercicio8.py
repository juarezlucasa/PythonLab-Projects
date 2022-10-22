"""
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada
"""


def alta(lista):
    # Genero una tupla con los valores de la compra y luego la subo a una lista
    producto = str(input("Ingrese nombre del producto: "))
    cantidad = int(input("Ingrese cantidad adquitida: "))
    importe = int(input("Ingrese importe por el total adquirido del producto: "))
    tupla = (producto, cantidad, importe)
    lista.append(tupla)
    print("Producto ingresado con éxito")


def baja(producto, lista):
    tupla_a_eliminar = consulta(producto, lista)
    lista.remove(tupla_a_eliminar)
    print("Producto Eliminado")


def consulta(producto, lista):
    for i in lista:
        if producto in i:
            print(i)
            return i
    else:
        print("Producto no encontrado")


def modificar(lista):
    producto = str(input("Ingrese nombre del producto a modificar: "))
    tupla_a_modificar = consulta(producto, lista)
    indice = lista.index(tupla_a_modificar)
    producto_modif = str(input("Ingrese nuevo producto: "))
    cantidad_modif = str(input("Ingrese nueva cantidad: "))
    importe_modif = str(input("Ingrese nuevo importe: "))
    nueva_tupla = (producto_modif, cantidad_modif, importe_modif)
    lista[indice] = nueva_tupla
    print("Producto modificado")
    print(lista)


lista = []
# Genero un menu para entrar en cada una de las funciones.
print("---" * 50)
print("Menu del programa \n")
print("1 - Alta de producto")
print("2 - Baja de producto")
print("3 - Consulta de producto")
print("4 - Modificacion de producto")
print("9 - Salir \n")
opcion = int(input("ELIGE UNA OPCION: "))

while opcion != 9:
    if opcion == 1:
        alta(lista)
    if opcion == 2:
        producto = str(input("Ingrese nombre del producto a eliminar: "))
        baja(producto, lista)
    if opcion == 3:
        producto = str(input("Ingrese nombre del producto a consultar: "))
        indice = consulta(producto, lista)
    if opcion == 4:
        modificar(lista)
    if opcion == 9:
        break
    opcion = int(input("ELIGE UNA OPCION: "))
