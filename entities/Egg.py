import pygame
class Egg:
  def __init__(self, node, size):
    self.size = size
    self.node = node
    self.rect = pygame.Rect(node.x, node.y, size, size)
    self.deleted = False
    self.count = 0
  def lethal(self, snake):
    return self.count < 20
  def edible(self, snake):
    return self.count >= 20
  def update(self, screen):
    if self.count < 20: pygame.draw.rect(screen, (100,0,0), self.rect)
    else: pygame.draw.rect(screen, (0,100,0), self.rect)
  def move(self, nodes):
    if self.count >= 20: return
    self.count += 1
