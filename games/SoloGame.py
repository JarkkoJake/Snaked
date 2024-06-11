from entities import Snake
from menus import PauseMenu, DeathMenu

class SoloGame:
  score = 0
  player = None
  level = None
  get_fresh_level = None
  count = 0
  block_size = 0
  initialized = False
  paused = False

  def initialize(block_size, back_to_level_select, screen_width, screen_height):
    SoloGame.block_size = block_size
    if not PauseMenu.initialized: PauseMenu.initialize(lambda: SoloGame.set_paused(False), back_to_level_select, screen_width, screen_height)
    if not DeathMenu.initialized: DeathMenu.initialize(lambda: SoloGame.reset(), back_to_level_select, screen_width, screen_height)
    SoloGame.initialized = True
  
  def reset():
    SoloGame.paused = False
    if SoloGame.get_fresh_level == None: return
    SoloGame.level = SoloGame.get_fresh_level()
    SoloGame.player = Snake((250, 0, 0), SoloGame.level.nodes[1][2:18], 4, SoloGame.block_size)
    SoloGame.level.snakes.append(SoloGame.player)
    SoloGame.score = 0
    SoloGame.count = 0

  def update(screen, player_input):
    if not SoloGame.paused: SoloGame.count += 1
    if SoloGame.player == None or SoloGame.level == None:
      return
    
    if player_input.ESCAPE:
      if SoloGame.paused and SoloGame.player.dead:
        SoloGame.reset()
      else:
        SoloGame.paused = not SoloGame.paused

    if player_input.UP: SoloGame.player.turn(1)
    if player_input.RIGHT: SoloGame.player.turn(2)
    if player_input.DOWN: SoloGame.player.turn(3)
    if player_input.LEFT: SoloGame.player.turn(4)
    
    SoloGame.level.update(screen)
    if SoloGame.player.dead:
      SoloGame.paused = True
    if SoloGame.count >= 5:
      SoloGame.count = 0
      SoloGame.level.move()
    
    if SoloGame.paused and not SoloGame.player.dead:
      PauseMenu.update(screen, player_input)
    elif SoloGame.paused and SoloGame.player.dead:
      DeathMenu.update(screen, player_input)

  def set_paused(value):
    SoloGame.paused = value
