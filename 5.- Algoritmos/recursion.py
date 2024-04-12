#RECURSIÓN/ RECURSIVIDAD: Una función que se llama a sí misma
#1.- Caso base: el problema lo más simplificado/simple posible
#2.- Cómo vamos a estar avanzando
#3.- Volver llamar a la función

#Función que imprime N cantidad de veces la palabra "HOLA"
'''
hello(4)
n = 4
HOLA
hola(3)

hola(3)
n = 3
HOLA
hola(2)

hola(2)
n = 2
HOLA
hola(1)

hola(1)
n = 1
HOLA
hola(0)

hola(0)
n = 0
'''
def hola(n):
    if n > 0:
        print("HOLA")
        hola(n-1)

'''
Funcion de cuenta regresiva, reciba un número e imprima los números desde el que recibe hasta el 0
Ej: Recibo 10
Imprimir:
10 9 8 7 6 5 4 3 2 1 0

cuenta_regresiva(4)
num = 4
PRINT 4
cuenta_regresiva(3)

cuenta_regresiva(3)
num = 3
PRINT 3
cuenta_regresiva(2)

cuenta_regresiva(2)
num = 2
PRINT 2
cuenta_regresiva(1)

cuenta_regresiva(1)
num = 1
PRINT 1
cuenta_regresiva(0)

cuenta_regresiva(0)
num = 0
PRINT 0
cuenta_regresiva(-1)

cuenta_regresiva(-1)
num = -1
'''
def cuenta_regresiva(num):
    if num >= 0:
        print(num)
        cuenta_regresiva(num-1)

cuenta_regresiva(4)

#SIGMA - Recibe un número y va sumando todos los números anteriores
#sigma(5) = 5+4+3+2+1 = 15