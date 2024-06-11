import pygame
from entities import Node, Rock
from .BaseLevel import BaseLevel

class EmptyLevel(BaseLevel):
  COLOR = (230, 230, 230)
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
  