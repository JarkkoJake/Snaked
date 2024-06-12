import pygame
class MovingFood:
  def __init__(self, node, size, direction):
    self.size = size
    self.node = node
    self.rect = pygame.Rect(node.x + 1, node.y + 1, size-2, size-2)
    self.direction = direction
    self.deleted = False
  def lethal(self, snake):
    return False
  def edible(self, snake):
    return True
  def update(self, screen):
    pygame.draw.rect(screen, (0,100,0), self.rect)
  def move(self, nodes):
    next_row = self.node.y // self.size
    next_col = self.node.x // self.size
    if self.direction % 2 == 1:
      next_row += self.direction - 2
      if next_row < 0: next_row = len(nodes) - 1
      if next_row >= len(nodes): next_row = 0
    if self.direction % 2 == 0:
      next_col -= self.direction - 3
      if next_col < 0: next_col = len(nodes[0]) - 1
      if next_col >= len(nodes[0]): next_col = 0
    next_node = nodes[next_row][next_col]
    if next_node.entity or next_node.snake:
      if self.direction == 1: self.direction = 3
      elif self.direction == 2: self.direction = 4
      elif self.direction == 3: self.direction = 1
      elif self.direction == 4: self.direction = 2
    else:
      self.node.entity = None
      self.node = next_node
      self.node.entity = self
      self.rect = pygame.Rect(self.node.x, self.node.y, self.size, self.size)
