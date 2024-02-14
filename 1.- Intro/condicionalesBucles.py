#CONDICIONALES
x = 20
if x > 10: #== not = > < >= <=
    print("El numero ingresado es mayor a 10")
    print("El numero es:", x)
else:
    print("El numero es menor a 10")

edad_infante = 4
if edad_infante < 2:
    print("El infante es un bebe")
elif edad_infante < 5:
    print("El infante es un toddler")
else :
    print("El infante es un niño")


temperatura = 20
estaLloviendo = False
if temperatura > 18 and not estaLloviendo:
    print("Salgamos al parque")

edad = 17
permisoPadres = True
if edad > 18 or permisoPadres:
    print("Puede tener su licencia de manejo")

#BUCLES
for x in range(5): #Rango 0-4. 5 YA NO ENTRA for(var x=0; x<5; x++)
    print(x)

print("--------")

for y in range(5, 12): #(comienzo, fin) -> Fin no entramos. 5-11
    print(y)

print("--------")

for z in range(2, 12, 2): #(comienzo, fin, paso). 2-11 avanzando 2 en 2
    print(z)

lista_nombres = ["Elena", "Juana", "Pablo", "Pedro"]
for nombre in lista_nombres:
    print("El nombre es:", nombre)

#for(var i=0; i<lista_nombres.length; i++)
for i in range(len(lista_nombres)): #0 1 2 3 len(arreglo) = tamaño de lista
    print(f"Posicion:{i}. Valor:{lista_nombres[i]}")

estudiante = {
    "nombre": "Elena",
    "apellido": "De Troya",
    "edad": 19
}

#llave = "nombre"
#llave = "apellido"
#llave = "edad"
for llave in estudiante:
    print(llave, estudiante[llave])


inicio = 0
final = 5
while inicio < final:
    print("Inicio:", inicio, "Final:", final)
    inicio += 1
    final -= 1

#BREAK -> interrumpo por completo ciclo/bucle
for x in range(16):
    if x == 13:
        break
    print(x)

#CONTINUE -> interrupcion temporal . SALTO
for x in range(16):
    if x == 13:
        continue
    print(x)

texto = "Buen dia"
for caracter in texto:
    print(caracter)

#RETO INDIVIDUAL
#Dado el for 1 al 15, imprime todos los numeros EXCEPTO aquellos múltiples de 5
for x in range(1, 16):
    if x % 5 == 0: #Múltiple de 5
        continue
    print(x)

#Dada una cadena, imprima cada uno de los caracteres y que se detenga POR COMPLETO si encuentra un . (PUNTO)
cadena1 = "Hola, buenos dias. Como estas"
for y in cadena1:
    if y == ".":
        break
    print(y)