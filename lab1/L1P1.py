# Laboratorio 1 de Python
# -----------------------
#
# Problema 1
#
# Escriba un programa que a partir de una lista de strings en el formato:
#   ' nombre_apellido_dia-mes-año '
# genere 5 listas, una con los nombres, una con los apellidos, una con los 
# dias, una con los meses y finalmente una con los años de nacimiento.
#
# Ej: lista_inicial = [Claudio_Roman_01-01-1991, Rick_Grimes_09-05-1980]
#
# Al desear imprimir la lista de nombres, entregaría:
#
# >>> print nombres
# ['Claudio', 'Rick']
#
#
# ------------------------
# Ramiro Rebolledo Cormack
# ramrebol@gmail.com
# Miercoles 25/03/2015
#
lista_inicial = ['Claudio_Roman_01-01-1991, Rick_Grimes_09-05-1980']
aux   = lista_inicial[0]
lista = aux.split(',')

lista_nombres   = []
lista_apellidos = []
lista_dias      = []
lista_mes       = []
lista_agno      = []
fechas          = []

for fila in lista:
    aux = fila.split('_')
    lista_nombres.append(aux[0])
    lista_apellidos.append(aux[1])
    fechas = aux[2]
    #
    aux = fechas.split('-')
    lista_dias.append(aux[0])
    lista_mes.append(aux[1])
    lista_agno.append(aux[2])

