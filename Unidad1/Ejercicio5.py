# Escriba un programa que solicite un valor entero por pantalla y presente en la terminal del editor
# el valor incrementado en un 10%
NumeroEntero = int(input("Ingrese un numero por pantalla"))

Resultado = NumeroEntero + (NumeroEntero * 10 / 100)
print("Numero ingresado incrementado en un 10% : ")
print(Resultado)