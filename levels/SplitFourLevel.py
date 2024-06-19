import pygame
from entities import Rock
from .SplitCenterLevel import SplitCenterLevel

class SplitFourLevel(SplitCenterLevel):
  COLOR = (230, 230, 230)
  NAME = "Split Four Way"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
    centerIndex = len(self.nodes) // 2
    for node in self.nodes[centerIndex]:
      if node.entity == None:
        node.entity = Rock(node, block_size)
        self.entities.append(node.entity)
  