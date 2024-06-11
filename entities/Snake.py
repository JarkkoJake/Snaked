from .SnakeHead import SnakeHead
from .SnakeBlock import SnakeBlock
from .SnakeTail import SnakeTail

class Snake:
  def __init__(self, color, nodes, direction, block_size):
    self.color = color
    self.direction = direction

    self.snake_blocks = []

    for node in nodes:
      if len(self.snake_blocks) == 0: self.snake_blocks.append(SnakeHead(node.x, node.y, block_size, self.color, None, direction))
      else: self.snake_blocks.append(SnakeBlock(node.x, node.y, block_size, self.color, self.snake_blocks[-1], None))
    self.snake_blocks[-1] = SnakeTail(nodes[-1].x, nodes[-1].y, block_size, self.color, self.snake_blocks[-2])
  
  def get_length(self):
    return len(self.snake_blocks)
  
  def update(self, screen):
    for block in self.snake_blocks:
      block.update(screen)
  
  def turn(self, direction):
    if abs(self.direction - direction) == 2: return
    self.direction = direction
  
  def move(self):
    self.snake_blocks[0].direction = self.direction
    for block in self.snake_blocks:
      block.move()