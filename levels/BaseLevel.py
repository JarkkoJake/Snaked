import pygame
from entities import Node

class BaseLevel:
  COLOR = (230, 230, 230)
  def __init__(self, width, height, block_size):
    self.width = width
    self.height = height
    self.block_size = block_size
    self.entities = []
    self.snakes = []
    self.nodes = []
    for row in range(self.height // self.block_size):
      row_nodes = []
      for col in range(self.width // self.block_size):
        row_nodes.append(Node(col * self.block_size, row * self.block_size))
      self.nodes.append(row_nodes)
  
  def update(self, screen):
    pygame.draw.rect(screen, BaseLevel.COLOR, pygame.Rect(0, 0, self.width, self.height))
    for s in self.snakes:
      s.update(screen)
    self.entities = list(filter(lambda x: not x.deleted, self.entities))
    for e in self.entities:
      e.update(screen)
  
  def move(self):
    for s in self.snakes:
      s.move(self.nodes)
    for e in self.entities:
      e.move(self.nodes)