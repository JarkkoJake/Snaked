import pygame
from entities import Rock, Portal
from .SplitFourLevel import SplitFourLevel

class FourRoomPortalLevel(SplitFourLevel):
  COLOR = (230, 230, 230)
  NAME = "4 Rooms Portal"
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
    
    centerVertical = len(self.nodes) // 2
    centerHorizontal = len(self.nodes[0]) // 2

    portal1, portal2 = Portal.create_portal_pair(
      self.nodes[centerVertical // 2][centerHorizontal-2],
      self.nodes[centerVertical // 2][centerHorizontal+2],
      block_size,
      (200, 0, 0)
    )
    self.entities.append(portal1)
    self.entities.append(portal2)

    portal1, portal2 = Portal.create_portal_pair(
      self.nodes[-(centerVertical // 2)][centerHorizontal-2],
      self.nodes[-(centerVertical // 2)][centerHorizontal+2],
      block_size,
      (0, 200, 0)
    )
    self.entities.append(portal1)
    self.entities.append(portal2)

    portal1, portal2 = Portal.create_portal_pair(
      self.nodes[centerVertical - 2][centerHorizontal // 2],
      self.nodes[centerVertical + 2][centerHorizontal // 2],
      block_size,
      (0, 0, 200)
    )
    self.entities.append(portal1)
    self.entities.append(portal2)

    portal1, portal2 = Portal.create_portal_pair(
      self.nodes[centerVertical - 2][-(centerHorizontal // 2)],
      self.nodes[centerVertical + 2][-(centerHorizontal // 2)],
      block_size,
      (0, 200, 200)
    )
    self.entities.append(portal1)
    self.entities.append(portal2)
