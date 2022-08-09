"""
Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
fecha de jubilación, presente en la terminal el mensaje "Ya está en edad de jubilarse" en
caso contrario que presente "Aún está en edad de trabajar
"""

edad = int(input("Ingrese la edad del ser humano"))

if edad >= 65:
    print("El ser humano esta en condiciones de jubilarse")
else:
    print("No es momento de jubilarse aún.")
