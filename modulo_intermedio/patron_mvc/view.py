from tkinter import (
    StringVar,
    DoubleVar,
    Label,
    Tk,
    messagebox,
    Entry,
    Button,
    ttk,
    W,
    E,
)
from datetime import datetime
from xml.etree.ElementTree import tostring
from model import actualizar_treeview, alta, borrar, consultar

# ##############################################
# VISTA
# ##############################################
def mensaje_de_error(texto):
    messagebox.showerror("Error", texto)


root = Tk()
root.title("Presupuesto personal")

titulo = Label(root, text="v1.0", bg="RoyalBlue3", fg="thistle1", height=1, width=60)
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

today = datetime.today().strftime("%d/%m/%Y")


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
