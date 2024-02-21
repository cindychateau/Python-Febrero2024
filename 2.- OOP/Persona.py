class Persona:

    '''
    self = juana
    nombre = "Juana"
    apellido = "De Arco"
    email = "juana@codingdojo.com"
    hobbies = ["Bailar", "Programar"]
    '''
    #A través del método init INICIALIZAMOS/CREAMOS una nueva instancia
    def __init__(self, nombre, apellido, email, hobbies, edad, lineas_codigo):
        self.nombre = nombre #juana.nombre = "Juana"
        self.apellido = apellido #juana.apellido = "De Arco"
        self.email = email #juana.email = "juana@codingdojo.com"
        self.hobbies = hobbies #juana.hobbies = ["Bailar", "Programar"]
        self.edad = edad
        self.lineas_codigo = 0 #lineas de código que ha desarrollado
    
    #self -> la instancia que está invocando al método
    def saludar(self):
        print(f"Te saluda {self.nombre}, ¡Hola!")
    
    def cumpleanios(self):
        self.edad += 1
    
    #cantidad_lineas = 100
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas


