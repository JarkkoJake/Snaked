import pygame
from .BaseButton import BaseButton

class SettingsButton:
  def __init__(self, x, y, open_settings):
    self.rect = pygame.Rect(x, y, 100, 100)
    self.open_settings = open_settings
  def update(self, screen: pygame.Surface, player_input):
    hover = self.rect.collidepoint(player_input.MOUSE_X, player_input.MOUSE_Y)
    pygame.draw.rect(screen, BaseButton.BACKGROUND_COLOR_HOVER if hover else BaseButton.BACKGROUND_COLOR,\
      self.rect)
    if hover and player_input.MOUSE_DOWN:
      self.open_settings()