import random 
from snake import Snake 
from snake import snake_contains

seeded = 0

class Food: 
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def food_seed_random():
    if seeded == 0:
        random.seed()
        seeded = 1

# sorteia a posição da comida dentro do grid, não populando células que a cobra está ocupando 
def food_spawn(food: Food, snake: Snake, grid_width, grid_height) -> bool:
    if food is None and snake is None and grid_width <= 0 and grid_height <= 0:
        return False 
    
    if snake.lenght >= grid_width * grid_height:
        return False 
    
    while snake_contains(snake, x, y):
        x = random() % grid_width 
        y = random() % grid_height 
    
    food.x = x 
    food.y = y

    return True 