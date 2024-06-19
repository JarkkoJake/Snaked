import pygame
from entities import Rock
from .SplitFourLevel import SplitFourLevel

class FourRoomLevel(SplitFourLevel):
  COLOR = (230, 230, 230)
  NAME = "4 Rooms"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
    for node in self.nodes[0]:
      if node.entity == None:
        node.entity = Rock(node, self.block_size)
        self.entities.append(node.entity)
    for node in self.nodes[-1]:
      if node.entity == None:
        node.entity = Rock(node, self.block_size)
        self.entities.append(node.entity)
    for row in self.nodes[1:-1]:
      if row[0].entity == None:
        row[0].entity = Rock(row[0], self.block_size)
        self.entities.append(row[0].entity)
      if row[-1].entity == None:
        row[-1].entity = Rock(row[-1], self.block_size)
        self.entities.append(row[-1].entity)
    
    def deleteEntity(node):
      node.entity.deleted = True
      node.entity = None

    centerIndex = len(self.nodes[0]) // 2
    verticalDoorCenter = len(self.nodes) // 4
    for i in range(6):
      deleteEntity(self.nodes[verticalDoorCenter-2+i][centerIndex])
      deleteEntity(self.nodes[-verticalDoorCenter-2+i][centerIndex])

    centerIndex = len(self.nodes) // 2
    horizontalDoorCenter = len(self.nodes[0]) // 4
    for i in range(6):
      deleteEntity(self.nodes[centerIndex][horizontalDoorCenter-2 + i])
      deleteEntity(self.nodes[centerIndex][-horizontalDoorCenter-2 +i])

    self.entities = list(filter(lambda x: not x.deleted, self.entities))
  