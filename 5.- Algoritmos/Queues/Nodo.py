class Nodo:

    def __init__(self, valor):
        self.valor = valor
        self.next = None #Next se refiere al siguiente nodo de mi queue. Como mi nodo aún NO está en ninguna fila, entonces su siguiente en NONE