import pygame
import  random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'assets/{name}.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])

        self.current_image = 0

        self.animation_images = [self.get_image(0, 0), self.get_image(0, 0)]

        self.scale = 4

    def get_image(self, x, y, h=24):
        image = pygame.Surface([16, h])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, h))
        return image

    def animate(self):
        # next to the next image
        self.current_image = random.randint(0, 1)

        # update image from the current animation
        self.image = self.animation_images[self.current_image]
        self.image.set_colorkey([0, 0, 0])
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale,
                                                         self.image.get_height() * self.scale))