#def = define -> Definiendo una función
def saludo():
    print("¡Hola Mundo!")
    print("¡Heeey!")


saludo()
saludo()
saludo()

#nombre = "Juana"
def saludoNombre(nombre):
    print(f"¡Hola {nombre}!")

saludoNombre("Elena")
saludoNombre("Juana")

num1 = 10

#num1 = 4, num2 = 5
def sumatoria(num1, num2):
    print(num1+num2)

sumatoria(4, 5)

#num1 = 8, num2 = 9
def sumatoriaReturn(num1, num2):
    return num1+num2 #17

resultado_suma = sumatoriaReturn(8, 9) #17
multiplacion = resultado_suma*5
print("El resultado es:",resultado_suma)
print("El multiplicacion es:",multiplacion)

resultado_suma2 = sumatoriaReturn(10+5, 10)
print(resultado_suma2)

#Parámetro por Default -> En dado caso de que algún argumento NO se envíe, mi parametro funcionará por default
#nombre = "Juana". apellido = "De Arco"
def hello(nombre="Elena", apellido="De Troya"):
    print(f"¡Hola {nombre} {apellido}!") #print("¡Hola "+nombre+" "+apellido+"!")

hello()
hello("Juana")
hello("Juana", "De Arco")
hello(apellido="De Arco")

#Funcion que reciba un número, si es par que te regrese el num al cuadrado, si el impar que te regrese el num
def numeros(num):
    if num % 2 == 0: #PAR
        return num*num
    else:
        return num


#Función que reciba un arreglo y que regrese la suma de los valores del arreglo
#[1, 2, 3] 6
lista = []
def suma_array(arreglo):
    resultado = 0
    for num in arreglo:
        resultado += num
    return resultado

print(suma_array([1, 2, 3]))

#Función que reciba un arreglo y que regrese el número mayor del arreglo
#[1, 2, 3] 3
'''
arr = [1, 2, 3]
max = 1
num = 1
---
num = 2
max = 2
---
num = 3
max = 3
'''
def numero_mayor(arr):
    max = arr[0]
    for num in arr:
        if max < num:
            max = num
    return max

#Función que reciba un arreglo y reciba un número y regrese True si el número se encuentra dentro del arreglo o False si NO se encuentra en el arreglo
#[1, 2, 3], 3 -> TRUE. [1, 2, 3], 5 ->FALSE
'''
arr = [1, 2, 3]
num = 3
x = 1
x = 2
x = 3
<-True
================
arr = [1, 2, 3]
num = 4
x = 1
x = 2
x = 3
'''
def existe_numero(arr, num):
    existe = False
    for x in arr:
        if x == num:
            existe = True
    return existe

#Función que reciba un arreglo y reemplace cualquier número negativo por 0. Regresa el arreglo SIN números negativos. Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]
'''
arr = [1, 5, 10, -2]
range-> 0 - 3
i = 0
i = 1
i = 2
i = 3
arr[3] = 0
arr = [1, 5, 10, 0]
'''
def reemplaza_negativos(arr):
    for i in range(len(arr)): 
        if arr[i] < 0:
            arr[i] = 0 
    return arr

def reemplaza_negativos2(arr):
    nuevo_arreglo = []
    for valor in arr:
        if valor < 0:
            nuevo_arreglo.append(0)
        else:
            nuevo_arreglo.append(valor)
    
    return nuevo_arreglo