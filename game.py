import pygame
from player import Player

class Game():

    def __init__(self):

        # le joueur
        self.player = Player(self)

        # ensemble des touches utilisees
        self.pressed = {}

    def update(self, screen):

        #appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser l'animation du joueur
        self.player.animate()

        # verifier si le joueur souhaite bouger le vaisseau
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():
            self.player.move_down()
