"""
Trabajo Práctico Modulo 1 Inicial
Alumnos: Elías Santoro / Lucas Juarez
Fecha de entrega: 26/09/2022 23:59hs
"""

from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import re
from datetime import date
from xml.etree.ElementTree import tostring

# ##############################################
# MODELO
# ##############################################
"""class MiRex():

    def validar_producto(self,): pass

    def validar_precio(self,): pass

    def validar_cantidad(self,): pass"""


def mensaje_de_error(texto):
    messagebox.showerror("Error", texto)


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
        mensaje_de_error(error_message)
        # print(
        #     "ERROR: No ingrese ningún número de su Tarjeta de credito. Solo ingrese el nombre de la misma. \n El formato de fecha debe ser dd/mm/yyyyy Ej: 04/10/1992  "
        # )


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


# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("Presupuesto personal")

titulo = Label(root, text="v1.0", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)

producto = Label(root, text="Fecha")
producto.grid(row=1, column=0, sticky=W)
cantidad = Label(root, text="Tarjeta de credito")
cantidad.grid(row=2, column=0, sticky=W)
precio = Label(root, text="Descripcion del gasto")
precio.grid(row=3, column=0, sticky=W)
precio = Label(root, text="Cuota actual")
precio.grid(row=4, column=0, sticky=W)
precio = Label(root, text="Cuota final")
precio.grid(row=5, column=0, sticky=W)
precio = Label(root, text="Monto del gasto")
precio.grid(row=6, column=0, sticky=W)


# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val, d_val, e_val, f_val = (
    StringVar(),
    StringVar(),
    StringVar(),
    DoubleVar(),
    DoubleVar(),
    DoubleVar(),
)
w_ancho = 20

today = date.today()


entrada1 = Entry(root, textvariable=a_val, width=w_ancho)
entrada1.grid(row=1, column=1)
entrada1.insert(0, today)
entrada2 = Entry(root, textvariable=b_val, width=w_ancho)
entrada2.grid(row=2, column=1)
entrada3 = Entry(root, textvariable=c_val, width=w_ancho)
entrada3.grid(row=3, column=1)
entrada4 = Entry(root, textvariable=d_val, width=w_ancho)
entrada4.grid(row=4, column=1)
entrada5 = Entry(root, textvariable=e_val, width=w_ancho)
entrada5.grid(row=5, column=1)
entrada6 = Entry(root, textvariable=f_val, width=w_ancho)
entrada6.grid(row=6, column=1)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
tree.column("#0", width=10, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=80)
tree.column("col2", width=150, minwidth=80)
tree.column("col3", width=350, minwidth=80)
tree.column("col4", width=100, minwidth=80)
tree.column("col5", width=100, minwidth=80)
tree.column("col6", width=150, minwidth=80)
tree.column("col7", width=100, minwidth=80)
tree.heading("#0", text="ID")
tree.heading("col1", text="Fecha")
tree.heading("col2", text="Tarjeta de credito")
tree.heading("col3", text="Descripcion")
tree.heading("col4", text="Cuota actual")
tree.heading("col5", text="Cuota final")
tree.heading("col6", text="Cuotas restantes")
tree.heading("col7", text="Monto")
tree.grid(row=10, column=0, columnspan=4)

boton_alta = Button(
    root,
    text="Crear gasto",
    command=lambda: alta(
        a_val.get(),
        b_val.get(),
        c_val.get(),
        d_val.get(),
        e_val.get(),
        f_val.get(),
        tree,
    ),
)
boton_alta.grid(row=1, column=2)

boton_consulta = Button(root, text="Consultar gastos", command=lambda: consultar(tree))
boton_consulta.grid(row=2, column=2)

boton_borrar = Button(root, text="Borrar gastos", command=lambda: borrar(tree))
boton_borrar.grid(row=3, column=2)
root.mainloop()
