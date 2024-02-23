from Animal import Animal

class Perro(Animal):

    def __init__(self, nombre, sonido, raza):
        super().__init__(nombre, sonido)
        self.raza = raza
    
    def ir_al_banio(self):
        print("Sale a pasear y el dueno lo recoje")