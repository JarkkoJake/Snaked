from games import *

class GameManager:

  game_mode = SoloGame
  level = None

  def set_game_mode(game_mode):
    GameManager.game_mode = game_mode
  
  def set_level(level):
    print("Selecting level: " + level)

  def update(screen, player_input):
    GameManager.game_mode.update(screen, player_input, GameManager.level)