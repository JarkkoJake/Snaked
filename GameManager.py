from games import *
from GameInfo import GameInfo

class GameManager:

  game_mode = SoloGame
  level = None

  def set_game_mode(game_mode, back_to_level_select):
    GameManager.game_mode = game_mode
    if not GameManager.game_mode.initialized:
      GameManager.game_mode.initialize(GameInfo.TILE_SIZE, back_to_level_select, GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT)
  
  def set_level(level):
    GameManager.level = level
    GameManager.game_mode.get_fresh_level = lambda: GameManager.level(GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT, GameInfo.TILE_SIZE)
    GameManager.game_mode.reset()

  def update(screen, player_input):
    GameManager.game_mode.update(screen, player_input)