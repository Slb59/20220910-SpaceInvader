import pygame
import math
import random

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        # charge l'image du vaisseau
        self.sprite_sheet = pygame.image.load('assets/ship.png')
        self.image = self.get_image_centre(0)
        self.image.set_colorkey([0, 0, 0])
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
        self.rect = self.image.get_rect()
        self.rect.x = math.ceil(SCREEN_WIDTH/2) - 10
        self.rect.y = SCREEN_HEIGHT - 150

        # gere l'animation du vaisseau
        self.current_image = 0

        self.images = {
            'droite1': [],
            'droite2': [],
            'centre': [self.get_image_centre(0), self.get_image_centre(25)],
            'gauche1': [],
            'gauche2': []
        }

        self.current_images = self.images['centre']

        # caractéristiques du vaisseau
        self.velocity = 5

        self.game = game


    def animate(self):
        # passer a l'image suivante
        self.current_image += random.randint(0, 1)

        # verifie si atteint la fin de l'animation
        if self.current_image >= len(self.current_images):
            self.current_image = 0

        # modifier l'image de l'animation courante
        self.image = self.current_images[self.current_image]
        self.image.set_colorkey([0, 0, 0])
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))


    def get_image_centre(self, pos):
        image = pygame.Surface([16, 24])
        image.blit(self.sprite_sheet, (0, 0), (32, pos, 16, 24))
        return image

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
