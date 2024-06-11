from games import *
from GameInfo import GameInfo

class GameManager:

  game_mode = SoloGame
  level = None

  def set_game_mode(game_mode):
    GameManager.game_mode = game_mode
  
  def set_level(level):
    GameManager.level = level
    GameManager.game_mode.level = GameManager.level(GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT, GameInfo.TILE_SIZE)
    GameManager.game_mode.reset(GameInfo.TILE_SIZE)

  def update(screen, player_input):
    GameManager.game_mode.update(screen, player_input)