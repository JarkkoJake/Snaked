from buttons import BaseButton
from levels import EmptyLevel, BorderedLevel

class LevelSelectMenu:
  initialized = False
  buttons = []

  def initialize(select_level, back_to_main_menu, screen_width, screen_height, settings_button):
    button_width = 400
    button_height = 75
    button_gap = 25
    button_x = round((screen_width / 2) - (button_width / 2))

    level_1_button = BaseButton(button_x, screen_height / 2 - button_height - button_gap / 2, button_width, button_height,\
      "Empty", lambda: select_level(EmptyLevel))
    level_2_button = BaseButton(button_x, screen_height / 2 + button_gap / 2, button_width, button_height,\
      "Bordered", lambda: select_level(BorderedLevel))

    
    back_button = BaseButton(button_x, screen_height - button_gap - button_height, button_width, button_height,\
      "Back", back_to_main_menu)


    LevelSelectMenu.buttons = [level_1_button, level_2_button, back_button, settings_button]
    LevelSelectMenu.initialized = True

  def update(screen, player_input):
    for butt in LevelSelectMenu.buttons:
      butt.update(screen, player_input)
