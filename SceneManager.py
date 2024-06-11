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
    MainMenu.initialize(lambda: SceneManager.set_game_mode(SoloGame), lambda: SceneManager.set_game_mode(MultiCollab),\
      lambda: SceneManager.set_game_mode(MultiVersus), GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT, SceneManager.settings_button)
    SceneManager.current_scene = MainMenu

  def update(screen, player_input):
    if SceneManager.current_scene != None:
      SceneManager.current_scene.update(screen, player_input)

  def set_game_mode(game_mode):
    GameManager.set_game_mode(game_mode, lambda: SceneManager.set_active_menu(LevelSelectMenu))
    if not LevelSelectMenu.initialized:
      LevelSelectMenu.initialize(SceneManager.select_level, lambda: SceneManager.set_active_menu(MainMenu), GameInfo.SCREEN_WIDTH,\
        GameInfo.SCREEN_HEIGHT, SceneManager.settings_button)
    SceneManager.set_active_menu(LevelSelectMenu)
  
  def set_active_menu(menu):
    SceneManager.current_scene = menu
  
  def select_level(level):
    GameManager.set_level(level)
    SceneManager.current_scene = GameManager

  def open_settings_menu():
    if not SettingsMenu.initialized:
      SettingsMenu.initialize(lambda: SceneManager.set_active_menu(MainMenu), GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT)
    SceneManager.set_active_menu(SettingsMenu)
