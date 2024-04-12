'''
FACTORIAL
Recibir un número y regresar el factorial de este
1! = 1*1 = 1
2! = 1*2 = 2
3! = 1*2*3 = 6
4! = 1*2*3*4 = 24
---
num = 4
numero_factorial = 1
1 - 4+1/4 -> 1, 2, 3, 4
i = 1
numero_factorial = 1*1 = 1
--
i = 2
numero_factorial = 1 * 2 = 2
--
i = 3
numero_factorial = 2 * 3 = 6
--
i = 4
numero_factorial = 6 * 4 = 24

RETURN 24
'''
def factorial(num):
    numero_factorial = 1
    for i in range(1, num+1):
        numero_factorial *= i
    return numero_factorial

print(factorial(4))


'''
FIBONACCI
Recibimos un número entero e imprimimos la serie de fibonacci en esa posición
Serie Fibonacci: Comenzando con 0 y 1, vamos sumando los dos últimos números
0 1 1 2 3 5 8 13 21 34 55 89
5 -> 0 1 1 2 3 5
--------
n = 4
lista_fibonacci = [0, 1]
2 - 5 -> 2, 3, 4
i = 2
siguiente_numero = lista_fibonacci[1] + lista_fibonacci[0] = 1 + 0 = 1
lista_fibonacci = [0, 1, 1]
-
i = 3
siguiente_numero = lista_fibonacci[2] + lista_fibonacci[1] = 1 + 1 = 2
lista_fibonacci = [0, 1, 1, 2]
-
i = 4
siguiente_numero = lista_fibonacci[3] + lista_fibonacci[2] = 2 + 1 = 3
lista_fibonacci = [0, 1, 1, 2, 3]
'''
def fibonacci(n):
    lista_fibonacci = [0, 1]
    for i in range(2, n+1):
        siguiente_numero = lista_fibonacci[i-1] + lista_fibonacci[i-2]
        lista_fibonacci.append(siguiente_numero)
    print(lista_fibonacci)

fibonacci(4)

'''
PALINDROMO
Recibimos una cadena y nos regresa True o False si la palabra es palíndroma
Ejemplo: oso, salas, seres, radar
ana -> True
palabra = "alla"
inicio = 0
final = 3
palabra[0] != palabra[3] -> a != a
inicio = 1
final = 2
palabra[1] != palabra[2] -> l != l
inicio = 2
final = 1
'''
def palindromo(palabra):
    inicio = 0
    final = len(palabra) -1 #la última posición de mi letra

    while inicio < len(palabra) / 2: #Dividiendo a la mitad
        if palabra[inicio] != palabra[final]:
            return False
        else:
            inicio += 1
            final -= 1
    
    return True

print(palindromo("al..la"))