import pygame

class SnakeHead:
  def __init__(self, x, y, size, color, previous_block, direction):
    self.size = size
    self.rect = pygame.Rect(x, y, size, size)
    self.color = color
    self.bulk = False
    self.previous_block = previous_block
    self.direction = direction

  def move(self):
    if self.direction == 1: self.rect.y -= self.size
    if self.direction == 2: self.rect.x += self.size
    if self.direction == 3: self.rect.y += self.size
    if self.direction == 4: self.rect.x -= self.size

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.draw_rect())
  
  def draw_rect(self):
    return pygame.Rect(self.rect.x - 1, self.rect.y - 1, self.rect.width + 2, self.rect.height + 2)