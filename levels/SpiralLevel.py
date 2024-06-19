import pygame
from entities import Rock
from .BaseLevel import BaseLevel

class BorderedLevel(BaseLevel):
  COLOR = (230, 230, 230)
  NAME = "Spiral"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
    for node in self.nodes[0]:
      node.entity = Rock(node, self.block_size)
      self.entities.append(node.entity)
    for node in self.nodes[-1]:
      node.entity = Rock(node, self.block_size)
      self.entities.append(node.entity)
    for row in self.nodes[1:-1]:
      row[0].entity = Rock(row[0], self.block_size)
      self.entities.append(row[0].entity)
      row[-1].entity = Rock(row[-1], self.block_size)
      self.entities.append(row[-1].entity)
  