#Importamos la clase
from Persona import Persona

#inicializando la instancia
elena = Persona("Elena", "De Troya", "elena@codingdojo.com", ["Leer", "Estudiar", "Jugar"], 16)

#Inicializando la instancia
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", ["Bailar", "Programar"], 20)

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
