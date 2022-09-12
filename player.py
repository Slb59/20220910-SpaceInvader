import pygame
import animation
import random
from projectile import Projectile

class Player(animation.AnimateSprite):

    def __init__(self, game, x, y):
        super().__init__('ship')

        # load the ship image
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.images = {
            'right1': [self.get_image(48, 0), self.get_image(48, 24)],
            'right2': [self.get_image(64, 0), self.get_image(64, 24)],
            'center': [self.get_image(32, 0), self.get_image(32, 24)],
            'left1': [self.get_image(16, 0), self.get_image(16, 24)],
            'left2': [self.get_image(0, 0), self.get_image(0, 24)]
        }

        self.animation_images = self.images['center']
        self.len_key_pressed = 0

        # ship features
        self.velocity = 5
        self.health = 100
        self.max_health = 100
        self.all_projectiles = pygame.sprite.Group()

        self.game = game

    def launch_projectile(self):
        print('new projectile')
        self.all_projectiles.add(Projectile(self))

    def update_health_bar(self, surface):

        # draw the health bar
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y + 100, self.rect.width, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x, self.rect.y + 100,
                                                   int(self.rect.width * (self.health / self.max_health)),
                                                   7])

    def no_move(self):
        self.animation_images = self.images['center']
        self.len_key_pressed = 0

    def move_right(self):
        print(self.len_key_pressed)
        if self.len_key_pressed > 20:
            self.animation_images = self.images['right2']
        else:
            self.animation_images = self.images['right1']
        self.rect.x += self.velocity
        self.len_key_pressed += 1

    def move_left(self):
        print(self.len_key_pressed)
        if self.len_key_pressed < -10:
            self.animation_images = self.images['left2']
        else:
            self.animation_images = self.images['left1']

        self.rect.x -= self.velocity
        self.len_key_pressed -= 1

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
