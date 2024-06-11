import pygame

class SnakeBlock:
  def __init__(self, x, y, size, color, next_block, previous_block):
    self.size = size
    self.rect = pygame.Rect(x, y, size, size)
    self.color = color
    self.bulk = False
    self.next_block = next_block
    self.previous_block = previous_block
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
    if self.direction == 1: self.rect.y -= self.size
    if self.direction == 2: self.rect.x += self.size
    if self.direction == 3: self.rect.y += self.size
    if self.direction == 4: self.rect.x -= self.size
    self.calculate_direction()

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.draw_rect())
  
  def draw_rect(self):
    return pygame.Rect(self.rect.x + 1, self.rect.y + 1, self.rect.width - 2, self.rect.height - 2)