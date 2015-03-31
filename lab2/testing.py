import math

def cuadratica (a,b,c):
    x1 = ( -b-math.sqrt(b**2-4.0*a*c) ) / (2.0*a)
    x2 = ( -b+math.sqrt(b**2-4.0*a*c) ) / (2.0*a)
    #
    return x1,x2

def primtme ( cadena ):
    print cadena
    return
    
def agnade ( lista ):
    lista.append([1,2])
    return lista
    
def imprime ( nombre, edad=40 ):
    '''Esto es solo una funcion de prueba\n probando 1,2,3'''
    print 'tu nombre es: ', nombre
    print 'tu edad es: ', edad
    

