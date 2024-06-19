import pygame
from .BaseLevel import BaseLevel

class EmptyLevel(BaseLevel):
  COLOR = (230, 230, 230)
  NAME = "Empty"
  def __init__(self, width, height, block_size):
    super().__init__(width, height, block_size)
  