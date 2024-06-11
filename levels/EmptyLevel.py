import pygame

class EmptyLevel:
  COLOR = (230, 230, 230)
  def __init__(self, width, height, block_size):
    self.width = width
    self.height = height
    self.block_size = block_size
    self.entities = []
  
  def update(self, screen):
    pygame.draw.rect(screen, EmptyLevel.COLOR, pygame.Rect(0, 0, self.width, self.height))
    for e in self.entities:
      e.update(screen)
  
  def move(self):
    for e in self.entities:
      e.move()