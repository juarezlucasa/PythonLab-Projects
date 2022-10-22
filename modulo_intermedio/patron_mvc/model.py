import sqlite3
import re
import view

# ##############################################
# MODELO
# ##############################################
"""class MiRex():

    def validar_producto(self,): pass

    def validar_precio(self,): pass

    def validar_cantidad(self,): pass"""


def conexion():
    con = sqlite3.connect("mibase.db")
    return con


def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE gastos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             fecha varchar2(16) NOT NULL,
             tarjeta_credito varchar2(16),
             descripcion varchar2 NOT NULL,
             cuota_actual integer,
             cuota_final integer,
             monto real not null)
    """
    cursor.execute(sql)
    con.commit()


try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")


def alta(fecha, tarjeta_credito, desc, cuota_actual, cuota_final, monto, tree):
    cadena = tarjeta_credito
    patron = "^[A-Za-záéíóú]*$"  # regex para el campo tarjeta_credito
    patron2 = "^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"  # regex para campo fecha
    if re.match(patron, cadena) and re.match(patron2, fecha):
        print(fecha, tarjeta_credito, desc, cuota_actual, cuota_final, monto)
        con = conexion()
        cursor = con.cursor()
        data = (fecha, tarjeta_credito, desc, cuota_actual, cuota_final, monto)
        sql = "INSERT INTO gastos(fecha, tarjeta_credito, descripcion, cuota_actual, cuota_final, monto) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        actualizar_treeview(tree)
    else:
        error_message = "ERROR: No ingrese ningún número de su Tarjeta de credito. Solo ingrese el nombre de la misma. \n El formato de fecha debe ser dd/mm/yyyyy Ej: 04/10/1992"
        view.mensaje_de_error(error_message)


def consultar(tree):
    actualizar_treeview(tree)


def borrar(tree):
    valor = tree.selection()
    print(valor)  # ('I005',)
    item = tree.item(valor)
    print(
        item
    )  # {'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item["text"])
    mi_id = item["text"]

    con = conexion()
    cursor = con.cursor()
    # mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM gastos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT id, fecha, tarjeta_credito, descripcion, cuota_actual, cuota_final, monto FROM gastos ORDER BY id ASC"
    con = conexion()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for registro in resultado:
        print(registro)
        cuotas_restantes = calcular_cuotas_restantes(registro[4], registro[5])
        mitreview.insert(
            "",
            0,
            text=registro[0],
            values=(
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                cuotas_restantes,
                registro[6],
            ),
        )


def calcular_cuotas_restantes(cuota_actual, cuota_final):
    return cuota_final - cuota_actual
