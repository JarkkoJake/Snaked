import pygame
class Food:
  def __init__(self, node, size):
    self.size = size
    self.node = node
    self.rect = pygame.Rect(node.x, node.y, size, size)
    self.deleted = False
  def lethal(self, snake):
    return False
  def edible(self, snake):
    return True
  def update(self, screen):
    pygame.draw.rect(screen, (0,0,0), self.rect)
  def move(self):
    pass