import pygame
import math
import random

class Player(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        super().__init__()

        # charge l'image du vaisseau
        self.sprite_sheet = pygame.image.load('assets/ship.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        # gere l'animation du vaisseau
        self.current_image = 0

        self.images = {
            'right1': [self.get_image(48, 0), self.get_image(48, 24)],
            'right2': [self.get_image(64, 0), self.get_image(64, 24)],
            'center': [self.get_image(32, 0), self.get_image(32, 24)],
            'left1': [self.get_image(16, 0), self.get_image(16, 24)],
            'left2': [self.get_image(0, 0), self.get_image(0, 24)]
        }

        self.current_images = self.images['center']
        self.len_key_pressed = 0

        # caractéristiques du vaisseau
        self.velocity = 5
        self.health = 100
        self.max_health = 100

        self.game = game

    def update_health_bar(self, surface):

        # dessin de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 15, self.rect.y + 100, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 15, self.rect.y + 100, self.health, 7])

    def animate(self):
        # passer a l'image suivante
        self.current_image = random.randint(0, 1)

        # modifier l'image de l'animation courante
        self.image = self.current_images[self.current_image]
        self.image.set_colorkey([0, 0, 0])
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))


    def get_image(self, x, y):
        image = pygame.Surface([16, 24])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 24))
        return image

    def no_move(self):
        self.current_images = self.images['center']
        self.len_key_pressed = 0

    def move_right(self):
        print(self.len_key_pressed)
        if self.len_key_pressed > 20:
            self.current_images = self.images['right2']
        else:
            self.current_images = self.images['right1']
        self.rect.x += self.velocity
        self.len_key_pressed += 1

    def move_left(self):
        if self.len_key_pressed < -20:
            self.current_images = self.images['left2']
        else:
            self.current_images = self.images['left1']

        self.rect.x -= self.velocity
        self.len_key_pressed -= 1

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
