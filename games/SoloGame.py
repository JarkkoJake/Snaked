from entities import Snake, Food, Portal, MovingFood, Egg
import random
from menus import PauseMenu, DeathMenu
import pygame

class SoloGame:
  score = 0
  player = None
  level = None
  get_fresh_level = None
  count = 0
  block_size = 0
  initialized = False
  paused = False

  def initialize(block_size, game_settings, back_to_level_select, screen_width, screen_height):
    SoloGame.block_size = block_size
    SoloGame.game_settings = game_settings
    if not PauseMenu.initialized: PauseMenu.initialize(lambda: SoloGame.set_paused(False), back_to_level_select, screen_width, screen_height)
    if not DeathMenu.initialized: DeathMenu.initialize(lambda: SoloGame.reset(), back_to_level_select, screen_width, screen_height)
    SoloGame.initialized = True
  
  def reset():
    SoloGame.paused = False
    if SoloGame.get_fresh_level == None: return
    SoloGame.level = SoloGame.get_fresh_level()
    SoloGame.player = Snake(SoloGame.game_settings.player1Color, SoloGame.level.nodes[1][5:10], 4, SoloGame.block_size)
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
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(0, screen.get_height() - 70, screen.get_width(), 70))
    score_font = pygame.font.SysFont("Comic Sans MS", 35)
    text_surface = score_font.render("Score: " + str(len(SoloGame.player.snake_blocks)), False, SoloGame.player.color)
    screen.blit(text_surface, (40, screen.get_height() - 60))

    if SoloGame.player.dead:
      SoloGame.paused = True
    
    if SoloGame.count >= SoloGame.game_settings.speed:
      SoloGame.count = 0
      SoloGame.level.move()

      food_count = 0
      for e in SoloGame.level.entities:
        if isinstance(e, Portal): continue # Skip portals because edible function is also used for the teleport
        if e.edible(SoloGame.player): food_count += 1
      needs_food = SoloGame.game_settings.numberOfFood - food_count
      if needs_food > 0:
        available_nodes = []
        for row in SoloGame.level.nodes:
          for node in row:
            if node.snake == None and node.entity == None:
              available_nodes.append(node)
        while needs_food > 0:
          needs_food -= 1
          pick_node = available_nodes.pop(random.randrange(len(available_nodes)))
          roll = random.random()
          if roll < 0.2 and SoloGame.game_settings.flies:
            pick_node.entity = MovingFood(pick_node, SoloGame.block_size, random.choice([1, 2, 3, 4]))
          elif roll > 0.8 and SoloGame.game_settings.eggs:
            pick_node.entity = Egg(pick_node, SoloGame.block_size)
          else: pick_node.entity = Food(pick_node, SoloGame.block_size)
          SoloGame.level.entities.append(pick_node.entity)
        
    
    if SoloGame.paused and not SoloGame.player.dead:
      PauseMenu.update(screen, player_input)
    elif SoloGame.paused and SoloGame.player.dead:
      DeathMenu.update(screen, player_input)

  def set_paused(value):
    SoloGame.paused = value
