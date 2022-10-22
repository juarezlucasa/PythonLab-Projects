import pwinput

clave = "Qwerty12345."
intento = pwinput.pwinput("Ingrese una contraseña: ")

while intento != clave:
    print("Contraseña incorrecta.")
    intento = pwinput.pwinput("Ingrese contraseña: ")

print("Contraseña correcta")
