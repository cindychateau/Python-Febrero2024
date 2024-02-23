#Importamos la clase
from Persona import Persona
from Animal import Animal
from Gato import Gato

firulais = Animal("Firulais", "Woof")
firulais.hacer_sonido()

miu = Animal("Miu", "miaaaau")
miu.hacer_sonido()


#inicializando la instancia
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", ["Leer", "Estudiar", "Jugar"], 16, miu)

#Inicializando la instancia
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", ["Bailar", "Programar"], 20, firulais)

juana.mascota.hacer_sonido()

print(juana.apellido)
print(elena.email)

juana.saludar()
elena.saludar()

juana.cumpleanios()
print(juana.edad)

juana.codificar(10) #lineas_codigo = 10

elena.codificar(50) #lineas_codigo = 50
elena.codificar(100) #lineas_codigo = 150
print(elena.lineas_codigo)

print(Persona.lista_personas)
Persona.imprimir_personas()

if Persona.mayor_edad(elena.edad):
    print("Si es mayor")
else:
    print("No es mayor")

if Persona.mayor_edad(30):
    print("Si es mayor")
else:
    print("No es mayor")

michi = Gato("Michi", "meeeoow", "corto", "calico")

michi.hacer_sonido()