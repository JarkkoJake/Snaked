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

  W = False
  C_W = False
  P_W = False

  S = False
  C_S = False
  P_S = False

  A = False
  C_A = False
  P_A = False

  D = False
  C_D = False
  P_D = False

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
    PlayerInput.P_W = PlayerInput.C_W
    PlayerInput.P_S = PlayerInput.C_S
    PlayerInput.P_A = PlayerInput.C_A
    PlayerInput.P_D = PlayerInput.C_D

    # UPDATE CURRENT PRESSES
    keys = pygame.key.get_pressed()
    PlayerInput.C_UP = keys[pygame.K_UP]
    PlayerInput.C_DOWN = keys[pygame.K_DOWN]
    PlayerInput.C_LEFT = keys[pygame.K_LEFT]
    PlayerInput.C_RIGHT = keys[pygame.K_RIGHT]
    PlayerInput.C_ESCAPE = keys[pygame.K_ESCAPE]
    PlayerInput.C_MOUSE_DOWN = pygame.mouse.get_pressed()[0]
    PlayerInput.C_W = keys[pygame.K_w]
    PlayerInput.C_S = keys[pygame.K_s]
    PlayerInput.C_A = keys[pygame.K_a]
    PlayerInput.C_D = keys[pygame.K_d]

    # UPDATE CURRENT STATE (button press accounted for 1 update)
    (PlayerInput.MOUSE_X, PlayerInput.MOUSE_Y) = pygame.mouse.get_pos()
    PlayerInput.UP = (not PlayerInput.P_UP) and PlayerInput.C_UP
    PlayerInput.DOWN = (not PlayerInput.P_DOWN) and PlayerInput.C_DOWN
    PlayerInput.LEFT = (not PlayerInput.P_LEFT) and PlayerInput.C_LEFT
    PlayerInput.RIGHT = (not PlayerInput.P_RIGHT) and PlayerInput.C_RIGHT
    PlayerInput.ESCAPE = (not PlayerInput.P_ESCAPE) and PlayerInput.C_ESCAPE
    PlayerInput.MOUSE_DOWN = (not PlayerInput.P_MOUSE_DOWN) and PlayerInput.C_MOUSE_DOWN
    PlayerInput.W = (not PlayerInput.P_W) and PlayerInput.C_W
    PlayerInput.S = (not PlayerInput.P_S) and PlayerInput.C_S
    PlayerInput.A = (not PlayerInput.P_A) and PlayerInput.C_A
    PlayerInput.D = (not PlayerInput.P_D) and PlayerInput.C_D

