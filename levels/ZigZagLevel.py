import pygame
from entities import Rock
from .BorderedLevel import BorderedLevel

class ZigZagLevel(BorderedLevel):
  COLOR = (230, 230, 230)
  NAME = "ZigZag"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
    
    corridorWidth = len(self.nodes[0]) // 6
    for i in range(1, 6):
      if i % 2 == 1:
        for row in range(len(self.nodes)):
          if row > len(self.nodes) - corridorWidth: break
          node = self.nodes[row][corridorWidth * i]
          if node.entity == None:
            node.entity = Rock(node, block_size)
            self.entities.append(node.entity)
      else:
        for row in range(len(self.nodes)):
          if row < corridorWidth: continue
          node = self.nodes[row][corridorWidth * i]
          if node.entity == None:
            node.entity = Rock(node, block_size)
            self.entities.append(node.entity)
