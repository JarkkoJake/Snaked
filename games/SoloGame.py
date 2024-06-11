from entities import Snake

class SoloGame:
  score = 0
  player = None
  level = None
  get_fresh_level = None
  count = 0
  block_size = 0

  def reset(block_size):
    SoloGame.block_size = block_size
    if SoloGame.get_fresh_level == None: return
    SoloGame.level = SoloGame.get_fresh_level()
    SoloGame.player = Snake((250, 0, 0), SoloGame.level.nodes[1][2:18], 4, block_size)
    SoloGame.level.snakes.append(SoloGame.player)
    SoloGame.score = 0
    SoloGame.count = 0

  def update(screen, player_input):
    SoloGame.count += 1
    if SoloGame.player == None or SoloGame.level == None:
      return
    
    if player_input.UP: SoloGame.player.turn(1)
    if player_input.RIGHT: SoloGame.player.turn(2)
    if player_input.DOWN: SoloGame.player.turn(3)
    if player_input.LEFT: SoloGame.player.turn(4)
    
    SoloGame.level.update(screen)
    if SoloGame.player.dead:
      SoloGame.reset(SoloGame.block_size)
    if SoloGame.count >= 5:
      SoloGame.count = 0
      SoloGame.level.move()
    