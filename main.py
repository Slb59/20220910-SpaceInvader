import pygame
from game import Game

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 100

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# generer la fenetre du jeu
pygame.display.set_caption("Space Invader Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('assets/desert-background-looped.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT*2))

# charger le jeu
game = Game(screen)

running = True

background_loop_i = 0

while running:

    clock.tick(FPS)

    # mise a jour du jeu
    game.update()

    # mettre a jour l'ecran
    pygame.display.flip()

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

        # le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False






