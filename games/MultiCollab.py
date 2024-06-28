from entities import Snake, Food, Portal, MovingFood, Egg
import random
from menus import PauseMenu, DeathMenu
import pygame

class MultiCollab:
  score = 0
  player_1 = None
  player_2 = None
  level = None
  get_fresh_level = None
  count = 0
  block_size = 0
  initialized = False
  paused = False

  def initialize(block_size, game_settings, back_to_level_select, screen_width, screen_height):
    MultiCollab.block_size = block_size
    MultiCollab.game_settings = game_settings
    if not PauseMenu.initialized: PauseMenu.initialize(lambda: MultiCollab.set_paused(False), back_to_level_select, screen_width, screen_height)
    if not DeathMenu.initialized: DeathMenu.initialize(lambda: MultiCollab.reset(), back_to_level_select, screen_width, screen_height)
    MultiCollab.initialized = True
  
  def reset():
    MultiCollab.paused = False
    if MultiCollab.get_fresh_level == None: return
    MultiCollab.level = MultiCollab.get_fresh_level()
    nodes = MultiCollab.level.nodes
    MultiCollab.player_1 = Snake(MultiCollab.game_settings.player1Color, [nodes[5][3], nodes[4][3], nodes[3][3]], 3, MultiCollab.block_size)
    MultiCollab.player_2 = Snake(MultiCollab.game_settings.player2Color, [nodes[5][5], nodes[4][5], nodes[3][5]], 3, MultiCollab.block_size)
    MultiCollab.level.snakes.append(MultiCollab.player_1)
    MultiCollab.level.snakes.append(MultiCollab.player_2)
    MultiCollab.score = 0
    MultiCollab.count = 0

  def update(screen, player_input):
    if not MultiCollab.paused: MultiCollab.count += 1
    if MultiCollab.player_1 == None or MultiCollab.level == None or MultiCollab.player_2 == None:
      return
    
    if player_input.ESCAPE:
      if MultiCollab.paused and (MultiCollab.player_1.dead or MultiCollab.player_2.dead):
        MultiCollab.reset()
      else:
        MultiCollab.paused = not MultiCollab.paused

    if player_input.UP: MultiCollab.player_1.turn(1)
    if player_input.RIGHT: MultiCollab.player_1.turn(2)
    if player_input.DOWN: MultiCollab.player_1.turn(3)
    if player_input.LEFT: MultiCollab.player_1.turn(4)

    if player_input.W: MultiCollab.player_2.turn(1)
    if player_input.D: MultiCollab.player_2.turn(2)
    if player_input.S: MultiCollab.player_2.turn(3)
    if player_input.A: MultiCollab.player_2.turn(4)
    
    MultiCollab.level.update(screen)
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, screen.get_height() - 70, screen.get_width(), 70))
    score_font = pygame.font.SysFont("Comic Sans MS", 35)
    player_1_score = len(MultiCollab.player_1.snake_blocks)
    player_2_score = len(MultiCollab.player_2.snake_blocks)
    text_surface = score_font.render("Score: " + str(player_1_score + player_2_score) + "     Player 1: " + str(player_1_score) + " Player 2: " + str(player_2_score),
     False, (0,0,0))
    screen.blit(text_surface, (40, screen.get_height() - 60))

    if (MultiCollab.player_1.dead or MultiCollab.player_2.dead):
      MultiCollab.paused = True
    
    if MultiCollab.count >= MultiCollab.game_settings.speed:
      MultiCollab.count = 0
      MultiCollab.level.move()

      food_count = 0
      for e in MultiCollab.level.entities:
        if isinstance(e, Portal): continue # Skip portals because edible function is also used for the teleport
        if e.edible(MultiCollab.player_1): food_count += 1
      needs_food = MultiCollab.game_settings.numberOfFood - food_count
      if needs_food > 0:
        available_nodes = []
        for row in MultiCollab.level.nodes:
          for node in row:
            if node.snake == None and node.entity == None:
              available_nodes.append(node)
        while needs_food > 0:
          needs_food -= 1
          pick_node = available_nodes.pop(random.randrange(len(available_nodes)))
          roll = random.random()
          if roll < 0.2 and MultiCollab.game_settings.flies:
            pick_node.entity = MovingFood(pick_node, MultiCollab.block_size, random.choice([1, 2, 3, 4]))
          elif roll > 0.8 and MultiCollab.game_settings.eggs:
            pick_node.entity = Egg(pick_node, MultiCollab.block_size)
          else: pick_node.entity = Food(pick_node, MultiCollab.block_size)
          MultiCollab.level.entities.append(pick_node.entity)
        
    # kill both players if difference in lenght is too long
    diff = abs(len(MultiCollab.player_1.snake_blocks) - len(MultiCollab.player_2.snake_blocks))
    if diff > 5:
      MultiCollab.player_1.dead = True
      MultiCollab.player_2.dead = True
    if MultiCollab.paused and not (MultiCollab.player_1.dead or MultiCollab.player_2.dead):
      PauseMenu.update(screen, player_input)
    elif MultiCollab.paused and (MultiCollab.player_1.dead or MultiCollab.player_2.dead):
      DeathMenu.update(screen, player_input)

  def set_paused(value):
    MultiCollab.paused = value
