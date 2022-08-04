# Escriba un programa que solicite el radio de una circunferencia y permita calcular
# el area. Presente el resultado en la terminal del editor

radioCircunferencia = int(input("Ingrese el radio de la circunferencia"))
pi = 3.1416

resultado = pi * (radioCircunferencia * radioCircunferencia)
print("Area de la circunferencia segun el radio ingresado: ")
print(resultado)
