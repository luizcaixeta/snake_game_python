# armazena dados e o próximo nó da sequência 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

# iniciamos a lista vazia, por isso head é iniciado com None 
class LinkedList:
    def __init__(self):
        self.head = None 

# vamos inserir alguns elementos na lista

def insereNoFinal(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
        self.head = new_node 
        return 
    last = self.head 
    while last.next:
        last = last.next
    last.next = new_node  

def printList(self):
    temp = self.head 
    while temp:
        print(temp.data, end=' ')
        temp = temp.next 
    print()
