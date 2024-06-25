import pygame

class ButtonGroup:
  def __init__(self, x, y, text, buttons):
    self.text = text
    self.font = pygame.font.SysFont("Comic Sans MS", 30)
    self.text_surface = self.font.render(self.text, False, (0, 0, 0))
    self.buttons = buttons
    self.text_start = (x, y)

  def update(self, screen, player_input):
    screen.blit(self.text_surface, self.text_start)
    for butt in self.buttons:
      butt.update(screen, player_input)