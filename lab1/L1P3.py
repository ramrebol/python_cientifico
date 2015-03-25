# Laboratorio 1 de Python
# -----------------------
#
# Problema 3
#
# Escriba un programa que genere una lista con 500 numeros enteros desde
# el 1 hasta el 500, a partir de la primera lista genere una lista solo con
# los numeros primos entre el 1 y 500.
#
# ------------------------
# Ramiro Rebolledo Cormack
# ramrebol@gmail.com
# Miercoles 25/03/2015

lista = []
primos= []

for n in range(1,501):
    lista.append(n) # lista = [1,2,3,... 500]

primos.append(1)
primos.append(2)
aux = 1

for n in lista[2:]:
    for d in range(2,n):
        if n%d == 0:
            aux = 0 # -> n no es primo
            break
    if aux == 1:
        primos.append(n)
    aux = 1




            
    
