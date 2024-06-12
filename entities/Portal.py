import pygame

class Portal:
  def create_portal_pair(node1, node2, block_size, color = (0, 0, 200)):
    portal_1 = Portal(node1, block_size, color)
    portal_2 = Portal(node2, block_size, color)
    portal_1.pair = portal_2
    portal_2.pair = portal_1
    return portal_1, portal_2
  def __init__(self, node, block_size, color):
    self.node = node
    self.color = color
    self.rect = pygame.Rect(node.x, node.y, block_size, block_size)
    self.pair = None
    self.deleted = False
  def lethal(self, snake):
    return False
  def edible(self, snake):
    if self.pair:
      snake_head = snake.snake_blocks[0]
      snake_head.node.snake = None
      snake_head.node = self.pair.node
      snake_head.node.snake = snake_head
    return False
  def update(self, screen):
    pygame.draw.rect(screen, self.color, self.rect)
  def move(self):
    pass