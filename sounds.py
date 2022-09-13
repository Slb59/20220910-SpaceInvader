import pygame
import time

class SoundManager:

    def __init__(self):
        self.sounds = {
            'tir': pygame.mixer.Sound('assets/sounds/tir.ogg'),
            'explosion': pygame.mixer.Sound('assets/sounds/explosion.wav')
        }

    def play(self, name):
        self.sounds[name].play()

    def play_ambiant(self):
        pygame.mixer.music.load('assets/sounds/mixkit-space-game-668.mp3')
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(1)
