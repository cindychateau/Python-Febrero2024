#Para ejecutar en MAC: python3 nombre_archivo.py
#Para ejecutar en Windows: py nombre_archivo.py O python nombre_archivo.py
print("Hola mundo!")

#Booleans
boolean = True #True o False

#Numerales
num = 10 #entero
fl = 10.99 # flotante - Número con decimales

nuevo_float = float(num) #Forzando/transformando el número entero en flotante
print(nuevo_float)
nuevo_entero = int(fl) #Transformando el número flotante en entero
print(nuevo_entero)
print(round(fl)) #round(numero) me permite redondear

import random #Importando librería random
num_aleatorio = random.randint(2, 5) #Número aleatorio entre 2 y 5
print(num_aleatorio)

#Cadenas/Textos/Strings
string = "ABCDEFG"
nombre = "Juana"
apodo = "juanita"

print("Este es el alfabeto", string) #La coma me pega los dos textos separándolos con un espacio
print("Este es el alfabeto "+string) #+ concatenar tal cual están
print("Este es un numero", 10)
#print("Este es un numero "+10) #ERROR -> con + solo puedo concatenar textos
print("Este es un numero "+str(10)) # "10"
print(f"Este es el alfabeto {string}!") #print("Este es el alfabeto "+string+"!")
print(f"Les presento a {nombre}, le pueden llamar '{apodo}'.")

#Métodos de manipulación de cadenas
string2 = "hola mundo! soy Juana de Arco y hoy es 13 de Febrero"
print(string2.title()) #Primera letra de cada palabra va a ser mayúscula
print(string2.upper()) #Todo en mayúsculas
print(string2.lower()) #Todo en minúsculas
print(string2.count("oy")) #Me regresa cuántos "oy" hay en la cadena
print(string2.find("Hola")) #Devolver dónde comienza "mundo". Regresa -1 si no encuentra la cadena. Case-sensitive (me hace distinción entre mayúscula y minúscula)

#TUPLA. Muy parecido a una lista PERO no puede cambiar de valor
tupla1 = ("Elena", "Juana", "Pedro", "Pablo") #Paréntesis
print(tupla1[1])
#tupla1[0] = "Elenita" -> ERROR la tupla no puede ser cambiada
tupla2 = ("texto", 7, 10.3, False) #Puedo tener distintos tipos de datos

#LISTAS / ARRAYS / ARREGLOS
lista_vacia = [] #array vacío
lista_nombres = ["Hugo", "Paco", "Luis"] 
print(lista_nombres[2])
lista_nombres[1] = "Donald"
print(lista_nombres)
lista_nombres.pop() #Elimina el valor en la última posición
print(lista_nombres)
lista_nombres.pop(0) #Eliminando la posición indicada
print(lista_nombres)
lista_nombres.append("Mickey") #Agregando un elemento al final de la lista
print(lista_nombres)

lista_mix = ["texto", 11, True, 1.1, ["lista1", "lista2"]]
print(lista_mix[4][0])

#DICCIONARIO - Objetos en Javascript
estudiante = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "edad": 18,
    "soltera": True,
    "hobbies": ["leer", "comer", "salir al parque"]
}

print(estudiante["nombre"])
estudiante["edad"] = 19
print(estudiante)
estudiante["estatura"] = 1.67
print(estudiante)

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos MERN para Pedro?