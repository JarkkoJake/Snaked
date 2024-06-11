from .SnakeHead import SnakeHead
from .SnakeBlock import SnakeBlock
from .SnakeTail import SnakeTail

class Snake:
  def __init__(self, color, nodes, direction, block_size):
    self.color = color
    self.direction = direction
    self.block_size = block_size

    self.can_set_new_direction = True

    self.snake_blocks = []

    for node in nodes:
      if len(self.snake_blocks) == 0: self.snake_blocks.append(SnakeHead(node, block_size, self.color, direction))
      else: self.snake_blocks.append(SnakeBlock(node, block_size, self.color, self.snake_blocks[-1]))
    self.snake_blocks[-1] = SnakeTail(nodes[-1], block_size, self.color, self.snake_blocks[-2])
  
  def get_length(self):
    return len(self.snake_blocks)
  
  def update(self, screen):
    for block in self.snake_blocks:
      block.update(screen)
  
  def turn(self, direction):
    if not self.can_set_new_direction: return
    if abs(self.direction - direction) == 2: return
    self.direction = direction
    self.can_set_new_direction = False
  
  def move(self, nodes):
    self.snake_blocks[0].direction = self.direction
    current_head_node = self.snake_blocks[0].node
    head_node_row = current_head_node.y // self.block_size
    head_node_col = current_head_node.x // self.block_size
    if self.direction % 2 == 1:
      head_node_row += self.direction - 2
      if head_node_row >= len(nodes): head_node_row = 0
      elif head_node_row < 0: head_node_row = len(nodes)-1
    elif self.direction % 2 == 0:
      head_node_col -= (self.direction - 3)
      if head_node_col >= len(nodes[0]): head_node_col = 0
      elif head_node_col < 0: head_node_col = len(nodes[0]) - 1 
    next_head_node = nodes[head_node_row][head_node_col]
    self.snake_blocks[0].next_node = next_head_node

    for block in self.snake_blocks:
      block.move()

    self.can_set_new_direction = True
