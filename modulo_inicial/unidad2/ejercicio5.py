"""
Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una
función, de forma que la operación se realice dentro de la misma.
"""


def calcular_radio_circunferencia(radio_circunferencia, pi):
    resultado = 2 * pi * radio_circunferencia
    print("Radio de la circunferencia segun el radio ingresado: ", resultado)


def calcular_area_circunferencia(radio_circunferencia, pi):
    resultado = pi * (radio_circunferencia**2)
    print("Area de la circunferencia segun el radio ingresado: ", resultado)


def calcular_percentil_10(numero):
    resultado = numero + (numero * 10 / 100)
    print("El numero ingresado, sumandole el 10%, da un total de :", resultado)


radio_circunferencia = int(
    input("Ingrese el valor del radio de la circunferencia a calcular: ")
)
numero_a_incrementar = int(
    input("Ingrese el numero que quisiera incrementar en un 10%: ")
)
pi = 3.1416

calcular_radio_circunferencia(radio_circunferencia, pi)
calcular_area_circunferencia(radio_circunferencia, pi)
calcular_percentil_10(numero_a_incrementar)
