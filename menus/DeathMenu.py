from buttons import BaseButton

class DeathMenu:
  initialized = False
  buttons = []
  def initialize(reset, exit_game, screen_width, screen_height):
    button_width = 400
    button_height = 75
    button_gap = 25
    button_x = round((screen_width / 2) - (button_width / 2))

    reset_button = BaseButton(button_x, screen_height // 2 - button_gap // 2 - button_height, button_width, button_height, "Reset", reset)
    exit_button = BaseButton(button_x, screen_height // 2 + button_gap // 2, button_width, button_height, "Exit", exit_game)

    DeathMenu.buttons = [reset_button, exit_button]
    DeathMenu.initialized = True

  def update(screen, player_input):
    for butt in DeathMenu.buttons:
      butt.update(screen, player_input)