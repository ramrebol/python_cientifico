# modulo cargado en L2P1P2.py

def factorial(n):
    '''
    Entrada: un natural n.
    Salida : el factorial de un numero natural n.
    Ejemplo: factorial(3)=3*2*1=6
    '''
    salida = 1
    for i in xrange(1,n+1):
        salida *= i
    #
    return salida
#
#
def fibonacci(n):
    '''
    Entrada: un natural n.
    Salida : lista con los n primeros numeros de la secuencia de Fibonacci.
    Ejemplo: fibonacci(5)=[1, 1, 2, 3, 5]
    '''
    [f0,f1] = [1,1]
    salida = [f0]
    if n==1:
        return salida
    #
    salida.append(f1)
    if n==2:
        return salida
    #
    for i in xrange(n-2):
        aux = f0+f1
        f0  = f1
        f1  = aux
        #
        salida.append(aux)
    #
    return salida
#
