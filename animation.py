import pygame
import random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()

        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False




animations = {
            'ship_droite2': [],
            'ship_droite1': [],
            'ship_centre': [self.get_image_centre(0), self.get_image_centre(25)],
            'ship_gauche2': [],
            'ship_gauche1': []
}
