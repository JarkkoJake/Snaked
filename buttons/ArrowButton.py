import pygame
from .BaseButton import BaseButton

class ArrowButton:
  def __init__(self, x, y, increase, on_click):
    self.x = x
    self.y = y
    self.on_click = on_click
    self.rect = pygame.Rect(x, y, 60, 60)
    self.font = pygame.font.SysFont("Comic Sans MS", 30)
    self.text_surface = self.font.render("<" if increase == False else ">", False, (0, 0, 0))
    self.text_start_x = self.rect.x + self.rect.width / 2 - self.text_surface.get_rect().width / 2
    self.text_start_y = self.rect.y + self.rect.height / 2 - self.text_surface.get_rect().height / 2
  def update(self, screen, player_input):
    hover = self.rect.collidepoint(player_input.MOUSE_X, player_input.MOUSE_Y)
    pygame.draw.rect(screen, BaseButton.BACKGROUND_COLOR_HOVER if hover else BaseButton.BACKGROUND_COLOR, self.rect)
    screen.blit(self.text_surface, (self.text_start_x, self.rect.y + 10))
    if hover and player_input.MOUSE_DOWN:
      self.on_click()