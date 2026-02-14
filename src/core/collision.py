from snake import Snake 

# verifica se a cabeça da cobra colidiu com o corpo da cobra. Se houver colisão retorna True
def check_collision(snake: Snake):
    if snake.length <= 1 or snake.head is None:
        return False 
    
    head_x = snake.head.x 
    head_y = snake.head.y 

    current = snake.head.next 
    while current is not None:
        if current.x == head_x and current.y == head_y:
            return True 
        current = current.next 

    return False 