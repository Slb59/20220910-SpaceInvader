import pygame
from pygame.locals import *

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# generer la fenetre du jeu
pygame.display.set_caption("Space Invader Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/desert-background-looped.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT*2))

running = True

background_loop_i = 0

while running:

    # appliquer l'arriere plan
    screen.fill((0, 0, 0))
    screen.blit(background, (0, background_loop_i))
    screen.blit(background, (0, background_loop_i - SCREEN_HEIGHT))
    if background_loop_i == SCREEN_HEIGHT:
        background_loop_i = 0
    background_loop_i += 1

    for event in pygame.event.get():


        # evenement fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()

    pygame.display.update()
    clock.tick(FPS)


