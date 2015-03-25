# Laboratorio 1 de Python
# -----------------------
#
# Problema 2
#
# - Escriba un programa que genere una lista con 20 numeros del 1 al 5 y que
#   imprima dicha lista.
# - Luego genere un diccionario que relacione el cada numero con su cantidad
#   de apariciones.
# - Finalmente imprima la ocurrencia de cada número, desde el mas repetido al
#   menos repetido.
#
# ------------------------
# Ramiro Rebolledo Cormack
# ramrebol@gmail.com
# Miercoles 25/03/2015
#
#
import random
lista = []

for n in range(20):
    lista.append(random.randint(1,5)) # numero aleatorio entre {1,2,3,4,5}

print 'Lista de 20 numeros aleatorios entre 1 y 5:\n'
print lista

dic = {}
for i in range(5):
      dic['Numero '+str(i)] = lista.count(i) # cuantas veces esta i en la lista

