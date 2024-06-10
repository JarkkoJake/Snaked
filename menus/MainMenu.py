from buttons import BaseButton

class MainMenu:
  initialized = False
  buttons = []
  def initialize(play_solo, play_multi_collab, play_multi_versus, screen_width, screen_height, settings_button):
    button_width = 400
    button_height = 75
    button_gap = 25
    button_x = round((screen_width / 2) - (button_width / 2))

    play_solo_button = BaseButton(button_x, screen_height / 2 - button_height - button_gap - button_height / 2,\
      button_width, button_height, "Solo", play_solo)
    play_collab_button = BaseButton(button_x, screen_height / 2 - button_height / 2, button_width, button_height,\
      "2 Player Collab", play_multi_collab)
    play_versus_button = BaseButton(button_x, screen_height / 2 + button_gap + button_height / 2, button_width,\
      button_height, "2 Player Versus", play_multi_versus)

    MainMenu.buttons = [play_solo_button, play_collab_button, play_versus_button, settings_button]
    MainMenu.initialized = True

  def update(screen, player_input):
    for butt in MainMenu.buttons:
      butt.update(screen, player_input)
