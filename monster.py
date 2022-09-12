import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, x, y):

        super().__init__('enemy-small')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.animation_images = [self.get_image(0, 0), self.get_image(16, 0)]

        self.game = game

        # set variables for moving
        self.move_counter = 0
        self.move_direction = 1


    def move(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


