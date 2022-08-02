import sys
# Cree un programa que incorpore el modulo sys, al cual desde la terminal se le puedan pasar tres parametros. El programa debe tomar los parametros
# e indicar en la terminal si son multiplos de dos.
print("En funcion de los params recibidos, el mismo determinara si los mismos")
print("son multiplos de 2 ") 

PrimerParametro = int(sys.argv[1])
SegundoParametro = int(sys.argv[2])
TercerParametro = int(sys.argv[3])
NumeroMultiplo = 2

print(PrimerParametro)
print(PrimerParametro % NumeroMultiplo == 0)

print(SegundoParametro)
print(SegundoParametro % NumeroMultiplo == 0)

print(TercerParametro)
print(TercerParametro % NumeroMultiplo == 0)