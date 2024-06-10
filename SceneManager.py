from menus import *
from games import *
from buttons import SettingsButton
from GameManager import GameManager
from GameInfo import GameInfo

class SceneManager:

  current_scene = None
  settings_button = None
  def initialize():
    SceneManager.settings_button = SettingsButton(GameInfo.SCREEN_WIDTH - 120, 20, SceneManager.open_settings_menu)
    MainMenu.initialize(SceneManager.select_solo_game, SceneManager.select_multi_collab_game, SceneManager.select_multi_versus_game,\
      GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT, SceneManager.settings_button)
    SceneManager.current_scene = MainMenu

  def update(screen, player_input):
    if SceneManager.current_scene != None:
      SceneManager.current_scene.update(screen, player_input)

  def select_solo_game():
    print("solo")

  def select_multi_collab_game():
    print("multi")

  def select_multi_versus_game():
    print("vs")

  def open_settings_menu():
    print("settings")
