from Animal import Animal
#class Hijo(Padre):
class Gato(Animal):

    def __init__(self, nombre, sonido, tipo_pelaje, raza):
        super().__init__(nombre, sonido)
        self.tipo_pelaje = tipo_pelaje
        self.raza = raza
    
    def ir_al_banio(self):
        print("Va a su caja de arena y va al bano")
    
    #Sobreescritura/Anulacion
    def hacer_sonido(self):
        print("El gatito te ve un momento, se aleja de ti y dice:",self.sonido)
    
