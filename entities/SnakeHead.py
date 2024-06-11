import pygame

class SnakeHead:
  def __init__(self, node, size, color, direction):
    self.size = size
    self.node = node
    self.previous_node = None
    self.next_node = None
    self.update_rect()
    self.color = color
    self.bulk = 3
    self.direction = direction
    self.previous_direction = None

  def move(self):
    if self.bulk > 0: self.bulk -= 1
    self.previous_node = self.node
    self.node = self.next_node
    self.node.snake = self
    self.previous_direction = self.direction
    self.update_rect()

  def update_rect(self):
    self.rect = pygame.Rect(self.node.x, self.node.y, self.size, self.size)

  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.draw_rect())
  
  def draw_rect(self):
    return pygame.Rect(self.rect.x - 1, self.rect.y - 1, self.rect.width + 2, self.rect.height + 2)