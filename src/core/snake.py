"""
A cobra começa o jogo com três segmentos: o primeiro sendo a cabeça, o segundo o corpo e o terceiro a cauda, se movendo em um grid bidmensional (x, y);
A cobra cresce uma unidade a cada comida que ela come. O jogo termina quando a cobra colidir com si mesma (derrota) ou ocupar toda a tela (vitória);
A cobra deve se mover automaticamente e o jogador deve controlar a dreção da cobra usando as setas do teclado;
A cobra é uma lista encadeada de segmentos, onde cada segmento tem uma posição (x, y) e uma direção (up, down, left, right);
A cabeça da cobra é o primeiro segmento da lista e a cauda é o último segmento 
A cada movimento da cobra, a poisção de cada segmento é atualizada para a posição do segmento anterior, e a cabeça da cobra é movida para a nova posição, assim:

                        posição atual da cobra: (x, y) -> nova posição da cobra (x + dx, y + dy)

Quando a cobra colidir com a parede ela aparece do outro lado da tela, ou seja, se a cobra colidir com a parede direita ela aparece na parede esquerda;
"""

GRID_WIDTH = 20
GRID_HEIGHT = 20

class Segment:
    def __init__(self, x: int, y: int, next = None):
        self.x = x
        self.y = y
        self.next = next 

class Snake:
    def __init__(self, head: Segment, tail: Segment, length: int):
        self.head = head
        self.tail = tail
        self.length = length

# cria a cobra com 1 segmento inicial na posição (x, y)
def create_snake(x: int, y: int) -> Snake:
    # cria o primeiro segmento
    segment = Segment(x, y)

    #head e tail apontam para o mesmo nó
    snake = Snake(
        head=segment,
        tail=segment,
        length=1
    )
    
    return snake 

# adiciona 1 segmento no fim da cobra (posição atual da cauda)
# não preciso verificar se a lista está vazia porque create_snake já cria uma lista com 1 elemento 
def grow_snake(self, x: int, y: int):
    new_segment = Segment(x, y)

    self.tail.next = new_segment 
    self.tail = new_segment 

    self.length += 1

def move_snake(self, dx: int, dy: int):

    prev_x = self.head.x 
    prev_y = self.head.y 

    new_x = prev_x + dx
    new_y = prev_y + dy 

    new_x = (new_x + GRID_WIDTH) % GRID_WIDTH 
    new_y = (new_y + GRID_HEIGHT) % GRID_HEIGHT 

    self.head.x = new_x 
    self.head.y = new_y

    current = self.head.next 
    while current is not None:
        temp_x = current.x 
        temp_y = current.y

        current.x = prev_x 
        current.y = prev_y 

        prev_x = temp_x 
        prev_y = temp_y 

        current = current.next 

