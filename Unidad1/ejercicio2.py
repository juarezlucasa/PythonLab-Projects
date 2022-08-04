import sys
# Cree un programa que incorpore el modulo sys, al cual desde la terminal se le puedan pasar tres parametros. El programa debe tomar los parametros
# e indicar en la terminal si son multiplos de dos.
print("En funcion de los params recibidos, el mismo determinara si los mismos")
print("son multiplos de 2 ") 

primerParametro = int(sys.argv[1])
segundoParametro = int(sys.argv[2])
tercerParametro = int(sys.argv[3])
numeroMultiplo = 2

print(primerParametro)
print(primerParametro % numeroMultiplo == 0)

print(segundoParametro)
print(segundoParametro % numeroMultiplo == 0)

print(tercerParametro)
print(tercerParametro % numeroMultiplo == 0)