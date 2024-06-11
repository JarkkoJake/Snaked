import pygame
from .SnakeBlock import SnakeBlock

class SnakeTail:
  def __init__(self, node, size, color, next_block):
    self.size = size
    self.rect = pygame.Rect(node.x, node.y, size, size)
    self.node = node
    self.color = color
    self.next_block = next_block
    self.calculate_direction()
  
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
    if self.next_block.bulk == 1:
      self.next_block.bulk = 0
      new_block = SnakeBlock(self.next_block.previous_node, self.size, self.color, self.next_block)
      self.next_block = new_block
      return new_block
    else:
      self.node.snake = None
      self.node = self.next_block.previous_node
      self.node.snake = self
      self.direction = self.next_block.previous_direction
      self.update_rect()

  def update_rect(self):
    self.rect = pygame.Rect(self.node.x, self.node.y, self.size, self.size)

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.draw_rect())
  
  def draw_rect(self):
    return pygame.Rect(self.rect.x + (1 if self.direction % 2 == 0 else round(self.size/4)),\
      self.rect.y + (1 if self.direction % 2 == 1 else round(self.size/4)),\
      (self.rect.width - 2) if self.direction % 2 == 0 else round(self.size / 2),\
      (self.rect.height - 2) if self.direction % 2 == 1 else round(self.size / 2))
  