from entities import Snake

class SoloGame:
  score = 0
  player = None
  level = None
  count = 0

  def reset(block_size):
    if SoloGame.level == None: return
    SoloGame.player = Snake((250, 0, 0), SoloGame.level.nodes[1][2:5], 4, block_size)
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
    if SoloGame.count >= 5:
      SoloGame.count = 0
      SoloGame.level.move()
    