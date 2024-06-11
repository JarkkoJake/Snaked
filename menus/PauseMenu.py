from buttons import BaseButton

class PauseMenu:
  initialized = False
  buttons = []
  def initialize(resume, exit_game, screen_width, screen_height):
    button_width = 400
    button_height = 75
    button_gap = 25
    button_x = round((screen_width / 2) - (button_width / 2))

    resume_button = BaseButton(button_x, screen_height // 2 - button_gap // 2 - button_height, button_width, button_height, "Resume", resume)
    exit_button = BaseButton(button_x, screen_height // 2 + button_gap // 2, button_width, button_height, "Exit", exit_game)

    PauseMenu.buttons = [resume_button, exit_button]
    PauseMenu.initialized = True

  def update(screen, player_input):
    for butt in PauseMenu.buttons:
      butt.update(screen, player_input)