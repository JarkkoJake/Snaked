import pygame
class Rock:
  def __init__(self, node, size):
    self.size = size
    self.node = node
    self.rect = pygame.Rect(node.x, node.y, size, size)
    self.deleted = False
  def lethal(self, snake):
    return True
  def edible(self, snake):
    return False
  def update(self, screen):
    pygame.draw.rect(screen, (40,40,40), self.rect)
  def move(self):
    pass