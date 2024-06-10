import pygame
from SceneManager import SceneManager
from GameInfo import GameInfo
from PlayerInput import PlayerInput

pygame.init()
screen = pygame.display.set_mode((GameInfo.SCREEN_WIDTH, GameInfo.SCREEN_HEIGHT))
pygame.display.set_caption(GameInfo.TITLE)
pygame.font.init()
clock = pygame.time.Clock()
running = True

SceneManager.initialize()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((230, 230, 230))

    PlayerInput.update()

    SceneManager.update(screen, PlayerInput)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()