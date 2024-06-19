import pygame
from entities import Rock
from .BaseLevel import BaseLevel

class SplitCenterLevel(BaseLevel):
  COLOR = (230, 230, 230)
  NAME = "Split"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
    centerIndex = len(self.nodes[0]) // 2
    for row in self.nodes:
      centerNode = row[centerIndex]
      centerNode.entity = Rock(centerNode, block_size)
      self.entities.append(centerNode.entity)
  