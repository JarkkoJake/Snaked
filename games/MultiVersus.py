from entities import Snake, Food, Portal, MovingFood, Egg
import random
from menus import PauseMenu, DeathMenu
import pygame

class MultiVersus:
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
    MultiVersus.block_size = block_size
    MultiVersus.game_settings = game_settings
    if not PauseMenu.initialized: PauseMenu.initialize(lambda: MultiVersus.set_paused(False), back_to_level_select, screen_width, screen_height)
    if not DeathMenu.initialized: DeathMenu.initialize(lambda: MultiVersus.reset(), back_to_level_select, screen_width, screen_height)
    MultiVersus.initialized = True
  
  def reset():
    MultiVersus.paused = False
    if MultiVersus.get_fresh_level == None: return
    MultiVersus.level = MultiVersus.get_fresh_level()
    nodes = MultiVersus.level.nodes
    MultiVersus.player_1 = Snake(MultiVersus.game_settings.player1Color, [nodes[5][3], nodes[4][3], nodes[3][3]], 3, MultiVersus.block_size)
    MultiVersus.player_2 = Snake(MultiVersus.game_settings.player2Color, [nodes[5][5], nodes[4][5], nodes[3][5]], 3, MultiVersus.block_size)
    MultiVersus.level.snakes.append(MultiVersus.player_1)
    MultiVersus.level.snakes.append(MultiVersus.player_2)
    MultiVersus.score = 0
    MultiVersus.count = 0

  def update(screen, player_input):
    if not MultiVersus.paused: MultiVersus.count += 1
    if MultiVersus.player_1 == None or MultiVersus.level == None or MultiVersus.player_2 == None:
      return
    
    if player_input.ESCAPE:
      if MultiVersus.paused and (MultiVersus.player_1.dead or MultiVersus.player_2.dead):
        MultiVersus.reset()
      else:
        MultiVersus.paused = not MultiVersus.paused

    if player_input.UP: MultiVersus.player_1.turn(1)
    if player_input.RIGHT: MultiVersus.player_1.turn(2)
    if player_input.DOWN: MultiVersus.player_1.turn(3)
    if player_input.LEFT: MultiVersus.player_1.turn(4)

    if player_input.W: MultiVersus.player_2.turn(1)
    if player_input.D: MultiVersus.player_2.turn(2)
    if player_input.S: MultiVersus.player_2.turn(3)
    if player_input.A: MultiVersus.player_2.turn(4)
    
    MultiVersus.level.update(screen)
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, screen.get_height() - 70, screen.get_width(), 70))
    score_font = pygame.font.SysFont("Comic Sans MS", 35)
    player_1_score = len(MultiVersus.player_1.snake_blocks)
    player_2_score = len(MultiVersus.player_2.snake_blocks)
    text_surface = score_font.render("Player 1: " + str(player_1_score) + " Player 2: " + str(player_2_score),
     False, (0,0,0))
    screen.blit(text_surface, (40, screen.get_height() - 60))

    if (MultiVersus.player_1.dead or MultiVersus.player_2.dead):
      MultiVersus.paused = True
    
    if MultiVersus.count >= MultiVersus.game_settings.speed:
      MultiVersus.count = 0
      MultiVersus.level.move()

      food_count = 0
      for e in MultiVersus.level.entities:
        if isinstance(e, Portal): continue # Skip portals because edible function is also used for the teleport
        if e.edible(MultiVersus.player_1): food_count += 1
      needs_food = MultiVersus.game_settings.numberOfFood - food_count
      if needs_food > 0:
        available_nodes = []
        for row in MultiVersus.level.nodes:
          for node in row:
            if node.snake == None and node.entity == None:
              available_nodes.append(node)
        while needs_food > 0:
          needs_food -= 1
          pick_node = available_nodes.pop(random.randrange(len(available_nodes)))
          roll = random.random()
          if roll < 0.2 and MultiVersus.game_settings.flies:
            pick_node.entity = MovingFood(pick_node, MultiVersus.block_size, random.choice([1, 2, 3, 4]))
          elif roll > 0.8 and MultiVersus.game_settings.eggs:
            pick_node.entity = Egg(pick_node, MultiVersus.block_size)
          else: pick_node.entity = Food(pick_node, MultiVersus.block_size)
          MultiVersus.level.entities.append(pick_node.entity)
        
    # kill shorter player if difference in lenght is too long
    diff = abs(len(MultiVersus.player_1.snake_blocks) - len(MultiVersus.player_2.snake_blocks))
    if diff > 5:
      short_player = MultiVersus.player_1 if len(MultiVersus.player_1.snake_blocks) < len(MultiVersus.player_2.snake_blocks) else MultiVersus.player_2
      short_player.dead = True
    if MultiVersus.paused and not (MultiVersus.player_1.dead or MultiVersus.player_2.dead):
      PauseMenu.update(screen, player_input)
    elif MultiVersus.paused and (MultiVersus.player_1.dead or MultiVersus.player_2.dead):
      DeathMenu.update(screen, player_input)

  def set_paused(value):
    MultiVersus.paused = value
