# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal del editor
# el valor incrementado en un 10%
numeroEntero = int(input("Ingrese un numero por pantalla"))

resultado = numeroEntero + (numeroEntero * 10 / 100)
print("Numero ingresado incrementado en 10% : ")
print(resultado)
