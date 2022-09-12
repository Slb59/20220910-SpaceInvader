import pygame
from player import Player
import math

class Game():

    def __init__(self, screen):

        self.screen = screen

        # The player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self, math.ceil(self.screen.get_width()/2) - 10,  self.screen.get_height() - 150)
        self.all_players.add(self.player)

        # ensemble des touches utilisees
        self.pressed = {}

    def game_over(self):
        self.player.health = self.player.max_health

    def update(self):

        # setup player image
        self.screen.blit(self.player.image, self.player.rect)

        # update player animation
        self.player.animate()

        # update player health bar
        self.player.update_health_bar(self.screen)

        # move player projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
            projectile.animate()

        # setup projectiles images
        self.player.all_projectiles.draw(self.screen)

        # check ship movements
        if self.pressed.get(pygame.K_RIGHT) \
                and self.player.rect.x + self.player.rect.width < self.screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) \
                and self.player.rect.y + self.player.rect.height < self.screen.get_height():
            self.player.move_down()
        else:
            self.player.no_move()
