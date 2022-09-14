import pygame
import animation
from monsterbullets import MonsterBullet
from explosion import Explosion

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

        self.all_bullets = pygame.sprite.Group()

    def damage(self):
        # setup explosion image
        self.game.all_explosions.add(Explosion(self.game, self.rect.centerx, self.rect.top))
        # play sound
        self.game.sound_manager.play('explosion')
        # kill the monster
        self.game.all_monsters.remove(self)
        # add a score points
        self.game.add_score()
        if len(self.game.all_monsters) == 0:
            self.game.game_over()

    def launch_bullet(self):
        self.all_bullets.add(MonsterBullet(self))

    def move(self):
        self.rect.x += self.move_direction
        self.move_counter += 1

        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction


