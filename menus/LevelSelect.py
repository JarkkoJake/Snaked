from buttons import BaseButton
from levels import EmptyLevel, BorderedLevel, SplitCenterLevel, SplitFourLevel, FourRoomLevel, FourRoomPortalLevel, ZigZagLevel

class LevelSelectMenu:
  initialized = False
  buttons = []

  def initialize(select_level, back_to_main_menu, screen_width, screen_height, settings_button):
    button_width = 400
    button_height = 50
    button_gap = 10
    button_x = round((screen_width / 2) - (button_width / 2))

    back_button = BaseButton(button_x, screen_height - button_gap - button_height, button_width, button_height,\
      "Back", back_to_main_menu)

    empty_level_button = BaseButton(button_x, button_gap, button_width, button_height, EmptyLevel.NAME, lambda: select_level(EmptyLevel))
    bordered_level_button = BaseButton(button_x, button_gap * 2 + button_height, button_width, button_height, BorderedLevel.NAME, lambda: select_level(BorderedLevel))
    split_center_level_button = BaseButton(button_x, button_gap * 3 + button_height * 2, button_width, button_height, SplitCenterLevel.NAME, lambda: select_level(SplitCenterLevel))
    split_four_level_button = BaseButton(button_x, button_gap * 4 + button_height * 3, button_width, button_height, SplitFourLevel.NAME, lambda: select_level(SplitFourLevel))
    four_room_level_button = BaseButton(button_x, button_gap * 5 + button_height * 4, button_width, button_height, FourRoomLevel.NAME, lambda: select_level(FourRoomLevel))
    four_room_portal_level_button = BaseButton(button_x, button_gap * 6 + button_height * 5, button_width, button_height, FourRoomPortalLevel.NAME, lambda: select_level(FourRoomPortalLevel))
    zig_zag_level_button = BaseButton(button_x, button_gap * 7 + button_height * 6, button_width, button_height, ZigZagLevel.NAME, lambda: select_level(ZigZagLevel))

    LevelSelectMenu.buttons = [empty_level_button, bordered_level_button, split_center_level_button, split_four_level_button, four_room_level_button, four_room_portal_level_button, zig_zag_level_button, back_button, settings_button]
    LevelSelectMenu.initialized = True

  def update(screen, player_input):
    for butt in LevelSelectMenu.buttons:
      butt.update(screen, player_input)
