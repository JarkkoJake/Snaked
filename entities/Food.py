import pygame
class Food:
  def __init__(self, node, size):
    self.size = size
    self.node = node
    self.rect = pygame.Rect(node.x + 1, node.y + 1, size-2, size-2)
    self.deleted = False
  def lethal(self, snake):
    return False
  def edible(self, snake):
    return True
  def update(self, screen):
    pygame.draw.rect(screen, (0,100,0), self.rect)
  def move(self, nodes):
    pass