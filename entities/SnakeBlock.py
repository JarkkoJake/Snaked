import pygame

class SnakeBlock:
  def __init__(self, node, size, color, next_block):
    self.size = size
    self.node = node
    self.previous_node = None
    self.update_rect()
    self.color = color
    self.bulk = False
    self.next_block = next_block
    self.calculate_direction()
    self.previous_direction = None
  
  def calculate_direction(self):
    next_rect = self.next_block.rect
    """
      1 north
      2 east
      3 south
      4 west
    """
    if next_rect.y < self.rect.y: self.direction = 1
    if next_rect.x > self.rect.x: self.direction = 2
    if next_rect.y > self.rect.y: self.direction = 3
    if next_rect.x < self.rect.x: self.direction = 4

  def move(self):
    self.previous_node = self.node
    self.node = self.next_block.previous_node
    self.node.snake = self
    self.previous_direction = self.direction
    self.direction = self.next_block.previous_direction
    self.update_rect()
  
  def update_rect(self):
    self.rect = pygame.Rect(self.node.x, self.node.y, self.size, self.size)

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.draw_rect())
  
  def draw_rect(self):
    return pygame.Rect(self.rect.x + 1, self.rect.y + 1, self.rect.width - 2, self.rect.height - 2)