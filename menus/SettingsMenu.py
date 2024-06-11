from buttons import BaseButton

class SettingsMenu:
  initialized = False
  buttons = []

  def initialize(back_to_main_menu, screen_width, screen_height):
    button_width = 400
    button_height = 75
    button_gap = 25
    button_x = round((screen_width / 2) - (button_width / 2))

    
    back_button = BaseButton(button_x, screen_height - button_gap - button_height, button_width, button_height,\
      "Back", back_to_main_menu)

    SettingsMenu.buttons = [back_button]
    SettingsMenu.initialized = True

  def update(screen, player_input):
    for butt in SettingsMenu.buttons:
      butt.update(screen, player_input)
