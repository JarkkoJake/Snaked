from .SnakeHead import SnakeHead
from .SnakeBlock import SnakeBlock
from .SnakeTail import SnakeTail

class Snake:
  def __init__(self, color, x, y, direction, block_size):
    self.color = color
    self.direction = direction
    
    direction_delta_x = 0
    direction_delta_y = 0
    if direction % 2 == 0: direction_delta_x = block_size if direction == 4 else -block_size
    if direction % 2 == 1: direction_delta_y = block_size if direction == 1 else -block_size
    
    self.head = SnakeHead(x, y, block_size, self.color, None, direction)
    mid_block = SnakeBlock(x + direction_delta_x, y + direction_delta_y, block_size, self.color, self.head, None)
    self.tail = SnakeTail(x + 2 * direction_delta_x, y + 2 * direction_delta_y, block_size, self.color, mid_block)
    mid_block.previous_block = self.tail
    self.snake_blocks = [self.head, mid_block, self.tail]
  
  def get_length(self):
    return len(self.snake_blocks)
  
  def update(self, screen):
    for block in self.snake_blocks:
      block.update(screen)
  
  def turn(self, direction):
    if abs(self.direction - direction) == 2: return
    self.direction = direction
    print(self.direction)
  
  def move(self):
    self.head.direction = self.direction
    for block in self.snake_blocks:
      block.move()