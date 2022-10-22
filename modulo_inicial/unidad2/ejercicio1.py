import sys

# Cree un programa que incorpore el modulo sys, al cual desde la terminal se le puedan pasar tres parametros. El programa debe tomar los parametros
# e indicar en la terminal si son multiplos de dos.
# Utilizar clausula if/else

# Defino funcion esmultiplo para definir si un numero es multiplo de otro numero ingresado tambien por parametro


def esmultiplodedos(numero):
    resultado = numero % 2
    if resultado == 0:
        print("El numero ", numero, " es multiplo de 2")
    else:
        print("El numero ", numero, " NO es multiplo de 2")


print("En funcion de los params recibidos, el mismo determinara si los mismos")
print("son multiplos de 2 ")

primerParametro = int(sys.argv[1])
segundoParametro = int(sys.argv[2])
tercerParametro = int(sys.argv[3])

esmultiplodedos(primerParametro)
esmultiplodedos(segundoParametro)
esmultiplodedos(tercerParametro)
