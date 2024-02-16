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