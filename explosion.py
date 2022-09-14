import animation
import pygame

class Explosion(animation.AnimateSprite):

    def __init__(self,game, x, y):
        super().__init__('explosion')

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.animation_images = [self.get_image(0, 0, 16),
                                 self.get_image(16, 0, 16),
                                 self.get_image(32, 0, 16),
                                 self.get_image(48, 0, 16)]

        self.game = game

        # setup explosion duration
        self.explosion_duration = 250
        self.last_explosion = pygame.time.get_ticks()

    def remove(self):
        self.game.all_explosions.remove(self)
