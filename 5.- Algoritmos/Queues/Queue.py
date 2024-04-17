from Nodo import Nodo

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, nuevo_nodo):
        #1.- Revisar si mi head estaba vacío. Entonces nuevo_nodo es el primero de la lista
        if self.head == None:
            self.head = nuevo_nodo
        else:
            #2.- Si existe algo en mi queue, al último nodo le pongo como siguiente el nuevo_nodo
            ultimo_nodo = self.tail
            ultimo_nodo.next = nuevo_nodo
        #3.- Establezco el nuevo_nodo como el final de mi queue
        self.tail = nuevo_nodo
    
    def dequeue(self):
        if self.head == self.tail:
            self.tail = None
        
        nodo_actual = self.head
        self.head = nodo_actual.next
        nodo_actual.next = None
        return nodo_actual
    
    def impresion(self):
        aux = self.head
        while aux != None:
            print(aux.valor)
            aux = aux.next