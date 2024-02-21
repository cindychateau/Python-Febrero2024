class Persona:

    escuela = "Coding Dojo"
    lista_personas = []

    '''
    self = juana
    nombre = "Juana"
    apellido = "De Arco"
    email = "juana@codingdojo.com"
    hobbies = ["Bailar", "Programar"]
    '''
    #A través del método init INICIALIZAMOS/CREAMOS una nueva instancia
    def __init__(self, nombre, apellido, email, hobbies, edad):
        self.nombre = nombre #juana.nombre = "Juana"
        self.apellido = apellido #juana.apellido = "De Arco"
        self.email = email #juana.email = "juana@codingdojo.com"
        self.hobbies = hobbies #juana.hobbies = ["Bailar", "Programar"]
        self.edad = edad
        self.lineas_codigo = 0 #lineas de código que ha desarrollado
        Persona.lista_personas.append(self)

    
    #self -> la instancia que está invocando al método
    def saludar(self):
        print(f"Te saluda {self.nombre}, ¡Hola!")
    
    def cumpleanios(self):
        self.edad += 1
    
    #cantidad_lineas = 100
    def codificar(self, cantidad_lineas):
        self.lineas_codigo += cantidad_lineas

    #Método que pertenece a mi clase y que llama o hace referencia a atributo de clase NO A INSTANCIAS
    @classmethod
    def imprimir_personas(cls):
        #persona = elena
        #persona = juana
        for p in cls.lista_personas:
            print(p.nombre, p.apellido)
    
    #Método estático: Algo que NO pertenece a la instancia, que NO pertenece a la clase, Ayuda/Organizar nuestro código
    @staticmethod
    def mayor_edad(edad):
        if edad > 17:
            return True
        else:
            return False