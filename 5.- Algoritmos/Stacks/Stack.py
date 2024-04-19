from Nodo import Nodo

class Stack:

    def __init__(self):
        self.top = None
    
    def push(self, nuevo_nodo):
        nuevo_nodo.next = self.top
        self.top = nuevo_nodo
    
    def pop(self):
        aux = self.top
        if aux != None:
            self.top = aux.next
            aux.next = None
    
    def impresion(self):
        aux = self.top
        while aux != None:
            print(aux.valor)
            aux = aux.next


            '''
            [(1*2) + (1-3)] * (1+3)
            '''