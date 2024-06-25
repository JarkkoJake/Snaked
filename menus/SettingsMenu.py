from buttons import BaseButton, ButtonGroup, ArrowButton
from GameSettings import GameSettings
from Colors import Colors

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
    

    player_1_color_blue_button = BaseButton(button_x, 150, 60, 60, "Blue", lambda: GameSettings.setPlayer1Color(Colors.BLUE))
    player_1_color_green_button = BaseButton(button_x + 70, 150, 60, 60, "Green", lambda: GameSettings.setPlayer1Color(Colors.GREEN))
    player_1_color_red_button = BaseButton(button_x + 140, 150, 60, 60, "Red", lambda: GameSettings.setPlayer1Color(Colors.RED))
    player_1_color_group = ButtonGroup(button_x, 100, "Player 1 Color", [player_1_color_blue_button, player_1_color_green_button, player_1_color_red_button])

    speed_decrease_button = ArrowButton(button_x, 260, False, lambda: GameSettings.changeSpeed(False))
    speed_increase_button = ArrowButton(button_x + 70, 260, True, lambda: GameSettings.changeSpeed(True))
    speed_group = ButtonGroup(button_x, 220, "Speed", [speed_decrease_button, speed_increase_button])

    food_count_decrease_button = ArrowButton(button_x, 360, False, lambda: GameSettings.changeNumberOfFood(False))
    food_count_increase_button = ArrowButton(button_x + 70, 360, True, lambda: GameSettings.changeNumberOfFood(True))
    food_group = ButtonGroup(button_x, 320, "Food Count", [food_count_decrease_button, food_count_increase_button])

    fly_button = BaseButton(button_x, 430, 400, 50, "Toggle flies", lambda: GameSettings.toggleFlies())
    egg_button = BaseButton(button_x, 490, 400, 50, "Toggle eggs", lambda: GameSettings.toggleEggs())

    SettingsMenu.buttons = [player_1_color_group, speed_group, food_group, fly_button, egg_button, back_button]
    SettingsMenu.initialized = True

  def update(screen, player_input):
    for butt in SettingsMenu.buttons:
      butt.update(screen, player_input)
