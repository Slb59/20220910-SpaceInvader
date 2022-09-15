import random

import pygame
from player import Player
import math
from sounds import SoundManager
from monster import Monster
from explosion import Explosion

class Game():

    def __init__(self, screen):

        self.screen = screen

        # The player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self, math.ceil(self.screen.get_width()/2) - 10,  self.screen.get_height() - 150)
        self.all_players.add(self.player)

        # set the monster group
        self.all_monsters = pygame.sprite.Group()

        # set the explosion group
        self.all_explosions = pygame.sprite.Group()

        # launch bullets
        self.bullet_cooldown = 500
        self.last_shoot = pygame.time.get_ticks()

        # ensemble des touches utilisees
        self.pressed = {}

        # manage sound
        self.sound_manager = SoundManager()

        # load the police
        self.score_font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.font1 = pygame.font.Font("assets/my_custom_font.ttf", 40)
        self.font2 = pygame.font.Font("assets/my_custom_font.ttf", 50)

        # set the score to 0
        self.score = 0

        # start counter
        self.countdown = 4
        self.last_countdown = pygame.time.get_ticks()

        # set if the game is playing
        self.is_game_over = False

    def add_score(self, points=10):
        self.score += points

    def start(self):
        self.sound_manager.play_ambiant()
        self.add_27_monsters()

    def game_over(self):
        # set the health to max
        self.player.health = self.player.max_health

        # delete all monsters
        self.all_monsters = pygame.sprite.Group()

        self.is_game_over = True
        self.countdown = 3

        self.add_27_monsters()

        self.all_explosions = pygame.sprite.Group()
        self.player.all_projectiles = pygame.sprite.Group()

    def add_27_monsters(self):
        for y in range(3):
            for x in range(9):
                self.all_monsters.add(Monster(self, 150 + 90*x, 50 + 90*y))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self):

        # setup player image
        self.screen.blit(self.player.image, self.player.rect)

        # update player animation
        self.player.animate()

        # update player health bar
        self.player.update_health_bar(self.screen)

        if self.countdown == 0 and not self.is_game_over:

            # draw the score
            score_text = self.score_font.render(f"Score : {self.score}", 1, (0, 0, 0))
            self.screen.blit(score_text, (20, 20))

            # move player projectiles
            for projectile in self.player.all_projectiles:
                projectile.move()
                projectile.animate()

            # animate explosion
            for explosion in self.all_explosions:
                time_now = pygame.time.get_ticks()
                if time_now - explosion.last_explosion > explosion.explosion_duration:
                    explosion.remove()
                else:
                    explosion.animate()

            self.all_explosions.draw(self.screen)

            # setup projectiles images
            self.player.all_projectiles.draw(self.screen)

            # setup an attaking monster
            time_now = pygame.time.get_ticks()
            if time_now - self.last_shoot > self.bullet_cooldown and len(self.all_monsters) > 0:
                alien = random.choice(self.all_monsters.sprites())
                alien.launch_bullet()
                self.last_shoot = time_now

            # update monsters
            for monster in self.all_monsters:
                monster.move()
                monster.animate()

                # setup bullets images
                monster.all_bullets.draw(self.screen)

                for bullet in monster.all_bullets:
                    bullet.move(self.screen)
                    bullet.animate()

            # setup monsters images
            self.all_monsters.draw(self.screen)

        elif self.countdown > 0 and not self.is_game_over:
            delay_text = self.font1.render(f"GET READY", 1, (0, 0, 0))
            self.screen.blit(delay_text, (
                math.ceil(self.screen.get_width() / 2) - 100,
                math.ceil(self.screen.get_height() / 2) - 100)
            )
            delay_value = self.font2.render(f"{self.countdown}", 1, (0, 0, 0))
            self.screen.blit(delay_value, (
                math.ceil(self.screen.get_width() / 2) - 40,
                math.ceil(self.screen.get_height() / 2) - 50)
            )
            count_timer = pygame.time.get_ticks()
            if count_timer - self.last_countdown > 1000:
                self.countdown -= 1
                self.last_countdown = count_timer

        elif self.countdown > 0 and self.is_game_over:
            text = self.font1.render(f"GAME OVER", 1, (0, 0, 0))
            self.screen.blit(text, (
                math.ceil(self.screen.get_width() / 2) - 100,
                math.ceil(self.screen.get_height() / 2) - 100)
                             )
            text = self.font1.render(f"Score : {self.score}", 1, (0, 0, 0))
            self.screen.blit(text, (
                math.ceil(self.screen.get_width() / 2) - 100,
                math.ceil(self.screen.get_height() / 2) - 30)
                             )
            count_timer = pygame.time.get_ticks()
            if count_timer - self.last_countdown > 1000:
                self.countdown -= 1
                self.last_countdown = count_timer

        # set the play again
        elif self.countdown == 0 and self.is_game_over:
            self.is_game_over = False
            # set the score to 0
            self.score = 0
            self.countdown = 4

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
