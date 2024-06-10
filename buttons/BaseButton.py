import pygame

class BaseButton:
  BACKGROUND_COLOR = (100, 100, 100)
  BACKGROUND_COLOR_HOVER = (150, 150, 150)
  def __init__(self, x, y, width, height, text, on_click):
    self.text = text
    self.on_click = on_click
    self.rect = pygame.Rect(x, y, width, height)
    self.font = pygame.font.SysFont("Comic Sans MS", 40)
    self.text_surface = self.font.render(self.text, False, (0, 0, 0))
    self.text_start_x = self.rect.x + self.rect.width / 2 - self.text_surface.get_rect().width / 2
    self.text_start_y = self.rect.y + self.rect.height / 2 - self.text_surface.get_rect().height / 2

  def update(self, screen, player_input):
    hover = self.rect.collidepoint(player_input.MOUSE_X, player_input.MOUSE_Y)
    pygame.draw.rect(screen, BaseButton.BACKGROUND_COLOR_HOVER if hover else BaseButton.BACKGROUND_COLOR, self.rect)
    screen.blit(self.text_surface, (self.text_start_x, self.rect.y + 10))
    if hover and player_input.MOUSE_DOWN:
      self.on_click()