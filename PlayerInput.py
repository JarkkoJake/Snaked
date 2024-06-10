import pygame

class PlayerInput:
  """
    Class that handles player input
    Prevents 1 button press from accounting as multiple inputs
  """

  UP = False
  C_UP = False
  P_UP = False

  DOWN = False
  C_DOWN = False
  P_DOWN = False

  LEFT = False
  C_LEFT = False
  P_LEFT = False

  RIGHT = False
  C_RIGHT = False
  P_RIGHT = False

  C_ESCAPE = False
  P_ESCAPE = False

  MOUSE_DOWN = False
  C_MOUSE_DOWN = False
  P_MOUSE_DOWN = False

  MOUSE_X = 0
  MOUSE_Y = 0

  def update():

    # UPDATE PREVIOUS BUTTONS
    PlayerInput.P_UP = PlayerInput.C_UP
    PlayerInput.P_DOWN = PlayerInput.C_DOWN
    PlayerInput.P_LEFT = PlayerInput.C_LEFT
    PlayerInput.P_RIGHT = PlayerInput.C_RIGHT
    PlayerInput.P_MOUSE_DOWN = PlayerInput.C_MOUSE_DOWN
    PlayerInput.P_ESCAPE = PlayerInput.C_ESCAPE

    # UPDATE CURRENT PRESSES
    PlayerInput.C_UP = pygame.K_UP
    PlayerInput.C_DOWN = pygame.K_DOWN
    PlayerInput.C_LEFT = pygame.K_LEFT
    PlayerInput.C_RIGHT = pygame.K_RIGHT
    PlayerInput.C_ESCAPE = pygame.K_ESCAPE
    PlayerInput.C_MOUSE_DOWN = pygame.mouse.get_pressed()[0]

    # UPDATE CURRENT STATE (button press accounted for 1 update)
    (PlayerInput.MOUSE_X, PlayerInput.MOUSE_Y) = pygame.mouse.get_pos()
    PlayerInput.UP = (not PlayerInput.P_UP) and PlayerInput.C_UP
    PlayerInput.DOWN = (not PlayerInput.P_DOWN) and PlayerInput.C_DOWN
    PlayerInput.LEFT = (not PlayerInput.P_LEFT) and PlayerInput.C_LEFT
    PlayerInput.RIGHT = (not PlayerInput.P_RIGHT) and PlayerInput.C_RIGHT
    PlayerInput.ESCAPE = (not PlayerInput.P_ESCAPE) and PlayerInput.C_ESCAPE
    PlayerInput.MOUSE_DOWN = (not PlayerInput.P_MOUSE_DOWN) and PlayerInput.C_MOUSE_DOWN
